# Write a Python program to list all files in a directory in Python.

# import OS module
import os

              #/Users/amitpandey/Desktop/nepal/0A030CF6-A967-4FC9-A3B2-35BE4D7E8D51_1_102_o.jpeg

import os

# Get the list of all files and directories
path = "/Users/amitpandey/Desktop/nepal/0A030CF6-A967-4FC9-A3B2-35BE4D7E8D51_1_102_o.jpeg"
dir_list = os.listdir(path)

print("Files and directories in '", path, "' :")

# prints all files
print(dir_list)