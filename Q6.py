Age = int(input("Enter your Age:"))
if (Age < 13):
    print("You are a child")
elif (13<= Age <=17):
    print("You are a teenager")
elif (18 <= Age <= 64):
    print("You are an adult")
else:
    print("You are a senior")
