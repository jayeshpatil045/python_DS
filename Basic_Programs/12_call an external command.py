import subprocess

# Define the command you want to run
command = ["echo", "Hello, World!"]

# Call the external command
result = subprocess.run(command, capture_output=True, text=True)

# Print the result
print("Return code:", result.returncode)
print("Output:", result.stdout)
print("Error (if any):", result.stderr)
