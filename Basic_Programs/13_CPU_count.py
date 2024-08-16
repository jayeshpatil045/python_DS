import multiprocessing

# Get the number of CPUs
cpu_count = multiprocessing.cpu_count()

# Print the number of CPUs
print("Number of CPUs available:", cpu_count)
