import os

# Specify the directory you want to list files from
directory = "D:\Bridgelab\python\Python_Basic\Functional_Programs"

# List all files in the specified directory
files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

# Print the list of files
print("Files in directory:", files)
