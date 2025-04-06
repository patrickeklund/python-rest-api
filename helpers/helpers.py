# Define Helpers as needed

# Import
import os, subprocess, stat

# Perform shell script
def runShellScript(script_path):
	current_directory = os.getcwd()
	file_path = os.path.join(os.getcwd(), script_path)
	st = os.stat(file_path)
	print("")
	print("# runScript", current_directory)
	print("- Current Working Directory: ", current_directory)
	print("- Running script: ", script_path)
	print("- Full path to file: ", file_path)
	print("- File rights: ", st)

	# Running the shell script
	try:
		os.chmod(file_path, st.st_mode | stat.S_IEXEC)
		result = subprocess.run([file_path], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
		print("Output:")
		print(result.stdout)  # Capture the standard output
		print("Error (if any):")
		print(result.stderr)  # Capture the standard error
	except subprocess.CalledProcessError as e:
		print(f"Error running script: {e}")
	except FileNotFoundError:
		print("Shell script not found. Please ensure the path is correct.")