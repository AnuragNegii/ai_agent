import os

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
