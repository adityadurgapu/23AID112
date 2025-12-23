#Creating a different Datatypes in python.
name = str(input("Enter  your name:"))
age = int(input("Enter your age:"))
height = float(input("Enter your height:"))
verify = (input("are you a student? (yes/no):"))

print("Your name is:",name)
print("Your height is:",height)
print("Your age is:",age)

if verify == "yes":
    print(name,"is a student")
else:
    print(name,"is not a student")