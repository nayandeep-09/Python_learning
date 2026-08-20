print ("Welcome to Practice Space! This is a simple program to help you practice coding. You can write your code here and test it out. Let's get started!")

input("Press Enter to continue...")
a = input("Please enter a number: ")
try:
    a = int(a)
    print(f"You entered the number: {a}")
except ValueError:
    print("That's not a valid number!") 
    