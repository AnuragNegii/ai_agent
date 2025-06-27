import os, subprocess

def run_python_file(working_directory, file_path, args=None):
    cwd = os.path.abspath(working_directory)
    new_file_path = os.path.abspath(os.path.join(cwd, file_path))

    if not new_file_path.startswith(cwd):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(file_path):
        return f'Error: File "{os.path.basename(file_path)}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{os.path.basename(file_path)}" is not a Python file.'

       
    try:
        result = subprocess.run(cwd=working_directory, args=["python3", file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
        if not result.stdout and not result.stderr and result.returncode == 0:
            return "No output produced"
        elif result.returncode != 0:
            return f"STDOUT: {result.stdout.decode('utf-8')}, STDERR: {result.stderr.decode('utf-8')}, Process exited with code {result.returncode}"
        else:
            return f"STDOUT: {result.stdout.decode('utf-8')}, STDERR: {result.stderr.decode('utf-8')}"
    except Exception as e:
        return f"Error: executing Python file: {e}"
