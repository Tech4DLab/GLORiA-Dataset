import os
import subprocess

def segment_fold():
    main_folder = os.getcwd()
    # Program to be executed inside each folder
    program_name = "segmentador_carpeta.py"

    for folder_path, _, files in os.walk(main_folder):
        if program_name in files:
            print(f"Running {program_name} in {folder_path}...")
            try:
                # Change to the directory where the program is located
                os.chdir(folder_path)

                # Run the Python program using subprocess
                result = subprocess.run(
                    ["python", program_name],
                    check=True,
                    capture_output=True,
                    text=True
                )
                print(f"Output from {program_name} in {folder_path}:\n{result.stdout}")

            except subprocess.CalledProcessError as e:
                print(f"Error running {program_name} in {folder_path}: {e.stderr}")

            finally:
                # Return to the main folder
                os.chdir(main_folder)

if __name__ == "__main__":
    segment_fold()
