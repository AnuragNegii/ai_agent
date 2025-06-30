import os
from google.genai import types

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

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
