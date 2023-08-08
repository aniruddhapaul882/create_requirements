import subprocess

def get_installed_packages():
    try:
        # Use subprocess to run pip list command and capture the output
        completed_process = subprocess.run(['pip', 'list'], capture_output=True, text=True)
        if completed_process.returncode == 0:
            # Split the output into lines and skip the header
            lines = completed_process.stdout.strip().split('\n')[2:]
            # Extract package names and versions
            packages = [line.split()[:2] for line in lines]
            return packages
        else:
            print("Error occurred while getting installed packages.")
            return []
    except Exception as e:
        print("Error occurred while getting installed packages:", e)
        return []

def write_requirements_file(packages, filename='requirements.txt'):
    with open(filename, 'w') as file:
        for package in packages:
            file.write(f"{package[0]}=={package[1]}\n")
    print(f"Successfully created {filename} with {len(packages)} packages.")

if __name__ == "__main__":
    installed_packages = get_installed_packages()
    if installed_packages:
        write_requirements_file(installed_packages)
    else:
        print("No packages found. Make sure you have Python packages installed.")
