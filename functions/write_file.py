import os
from google.genai import types

def write_file(working_directory, file_path, content):
    nwd= os.path.abspath(working_directory)

    file_path= os.path.join(nwd, file_path)
    file_path = os.path.abspath(file_path)

    if not file_path.startswith(nwd):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as E:
        return f'Erorr: "{E}"'

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to the given file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path":types.Schema(
                type=types.Type.STRING,
                description="Name of the file to which you want to write to."
            ),
            "content":types.Schema(
                type=types.Type.STRING,
                description="Content which you want to write to the file."
            )
        },
    ),
)
