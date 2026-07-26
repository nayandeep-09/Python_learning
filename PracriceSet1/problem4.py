#Q4. Write a python program to print the contents of a directory using the os module. Search online for the function which does that.

import os

# Specify the directory path
path = input("Enter directory path: ")

# Print the contents of the directory
contents = os.listdir(path)

print("Contents of the directory:")
for item in contents:
    print(item)

#to know the in which drive or in which path how many and which kind of files exit it just give names.