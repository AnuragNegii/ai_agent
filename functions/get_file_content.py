import os
from google.genai import types

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

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Read file contents",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
           "file_path": types.Schema(
                type=types.Type.STRING,
                description="Name of the file whoose content you have to check."
            ),
        },
    ),
)
