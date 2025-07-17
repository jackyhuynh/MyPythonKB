"""
    The structure of the testing
    my_flask_app/
    ├── .github/
    │   └── workflows/
    │       └── pylint.yml
    ├── source/
    │   └── simple_input_output/
    │       ├── classes.py
    │       └── test_main.py
    │   └── simple_flask/
    │       ├── classes.py
    │       └── test_main.py
"""
import os
import subprocess


def run_python_scripts(directory):
    """
    Recursively find and execute all Python scripts in the given directory that start with 'test_'.

    :param directory: The directory to search for Python scripts.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.startswith("test_") and file.endswith(".py"):
                print("---")
                file_path = os.path.join(root, file)
                print(f"Running {file_path}")
                result = subprocess.run(["python3", file_path],
                                        capture_output=True,
                                        text=True,
                                        check=False)
                if result.returncode != 0:
                    print(f"Error running {file_path}:\n{result.stderr}")
                else:
                    if result.stdout.strip():
                        print(f"Output from {file_path}:\n{result.stdout}")
                    else:
                        print(f"Test passed: {file_path}")


if __name__ == "__main__":
    SOURCE_DIRECTORY = "source"
    run_python_scripts(SOURCE_DIRECTORY)
