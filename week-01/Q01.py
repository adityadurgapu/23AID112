#Creating a different Datatypes in python.
name = (input("Enter  your name:"))
age = int(input("Enter your age:"))
height = float(input("Enter your height:"))
verify = (input("are you a student? (true/false):"))

print("Your name is:",name)
print("Your height is:",height)
print("Your age is:",age)

if (verify):
    print(name,"is a student")
else:
    print(name,"is not a student")
