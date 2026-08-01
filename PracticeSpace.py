#variables
#thing we want to store in memory we give them a particular name and space we can use that name to access the value stored in that variable.

a = 10
b = "nayan"
c = 10.20

print ("nayan")
print (a,b,c)
print (a)
print (b)
print (c)

#A,B and C are the container storing the values like 10, nayan and 10.20

#we can do calculation too

print("a + b =", a+c)

#=========================================================================

#data types
a = 1
# a is containing the number so the a is integer.
b = 10.20
# b containing the decimal number so the b is float.
c = "nayan"
# c is containing the string so the c is string.

print(a)
print(b)
print(c)

#A variable name can contain alphabets, digits, and underscores.
#A variable name can only start with an alphabet and underscores.
#A variable name can't start with a digit.
#No while space is allowed to be used inside a variable name.

#================================================================================================

#operators in python
#1. Arithmetic operators: +, -, *, / etc.
#2. Assignment operators: =, +=, -= etc.
#3. Comparison operators: ==, >, >=, <, != etc.
#4. Logical operators: and, or, not.

#1. Arithmetic operators: +, -, *, / etc.

a=10
b=20
c=10.11
d=20.09

print(a+b)
print(c+d)

print (b-a)
print (d-c)

#2. Assignment operators: =, +=, -= etc.

x = 5-2
x += 1 #its called x = x+1
print (x)

y=4*2
y-=2 #its called y = y-2
print(y)

#3. Comparison operators: ==, >, >=, <, != etc.
a= 10
b= 20

#this operator gives output in true or false according to condtion
print(a == b)
# It checks whether the value of a is equal to the value of b or not. If it is equal then it returns true otherwise false.
print(a > b)
# It checks whether the value of a is greater than the value of b or not. If it is greater then it returns true otherwise false.
print(a >= b)
# It checks whether the value of a is greater than or equal to the value of b or not. If it is greater or equal then it returns true otherwise false.
print(a < b)
# It checks whether the value of a is less than the value of b or not. If it is less then it returns true otherwise false.
print(a != b)
# It checks whether the value of a is not equal to the value of b or not. If it is not equal then it returns true otherwise false.


#4. Logical operators: and, or, not.
print(a and b)
# It checks whether the value of a and b is true or not. If both are true then it returns true otherwise false.
print(a or b)
# It checks whether the value of a or b is true or not. If either is true then it returns true otherwise false.
print(not a)
# It checks whether the value of a is false or not. If it is false then it returns true otherwise false.