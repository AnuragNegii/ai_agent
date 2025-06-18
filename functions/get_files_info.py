import os
from os.path import isdir

def get_files_info(working_directory, directory=None):
    values = []
    nwd= os.path.abspath(working_directory)

    if directory == None:
        directory = nwd 
    else:
        directory = os.path.join(nwd, directory)
        directory = os.path.abspath(directory)

    if not directory.startswith(nwd):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(directory):
        return f'Error: "{directory}" is not a directory'

    try :
        list_dir = os.listdir(directory)
        for dir in list_dir:
            new_dir = os.path.join(directory, dir)
            values.append(f"- {dir}: file_size={os.path.getsize(new_dir)} bytes, is_dir={os.path.isdir(new_dir)}")
    except Exception as e:
        return f"Error: {e}" 
    
    return "\n".join(values)

def get_file_content(working_directory, file_path):
    nwd = os.path.abspath(working_directory)
    
    file_path = os.path.join(working_directory, file_path)
    file_path = os.path.abspath(file_path)

    if not file_path.startswith(nwd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    MAX_CHARS = 10000
    file_content = ""
    try :
        with open(file_path, "r") as fp:
            file_content = fp.read(MAX_CHARS)
            if fp.read(1):
                file_content += f'[...File "{file_path}" truncated at 10000 characters]'
    except Exception as e:
        return f"Error: {e}"
    return file_content
