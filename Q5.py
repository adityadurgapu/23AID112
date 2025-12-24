#Ask inputs as strings.
str_1 = input(print("Enter your first number:"))
str_2 = input(print("Enter your second number:"))

#Make the strings into integers.
int_1 = int(str_1)
int_2 = int(str_2)

#Performing the operations with the inputs
print("The sum of the two numbers is:", int_1 + int_2)
print("The difference of the two numbers is:",int_1-int_2)
print("The product of two numbers is:", int_1*int_2)
if int_1 < int_2:
    print("Your first  number is less than your second number ")
elif int_1 == int_2:
    print("The entered numbers are same")
else:
    print("Your first number is greater than second number")