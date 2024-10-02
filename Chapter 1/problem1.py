import os

# Specify the directory path (use '.' for the current directory)
directory = './'

# List all contents of the directory
contents = os.listdir(directory)

# Print each item
for item in contents:
    print(item)
