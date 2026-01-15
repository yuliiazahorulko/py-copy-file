import subprocess


def copy_file(command: str) -> None:
    try:
        command_for_run, source_file, destination = command.split(" ")
    except ValueError:
        print("command = '' and nothing can be copied")
        return None

    if source_file == destination or command_for_run != "cp":
        return None

    try:
        subprocess.run([command_for_run, source_file, destination], check=True)
        print("Bash cp command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing bash command: {e}")
    except FileNotFoundError:
        print("Error: might be an issue with system path or OS.")
