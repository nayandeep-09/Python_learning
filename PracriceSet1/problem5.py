#Q5. Label the program written in problem 4 with comments.

import os
#import is jus a library for path checking and directory checking.
path = input("Enter directory path: ")
#path is a variable which is used to store the directory path entered by the user.
contents = os.listdir(path)
#contents is a variable which is used to store the list of files and directories in the specified path.
print("Contents of the directory:")
#prints the meesage "Contents of the directory:" to the console.
for item in contents:
#for loop takes every file and folders from the contents list and assigns it to the variable item. 
    print(item)
#just to print whatever in the contents list.