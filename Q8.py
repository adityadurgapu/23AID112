colour = input("What is the colour of the signal (Red/Yellow/green)").upper()
# Here upper command converts what user enters into upper case and satisfies conditons.
if (colour == "RED"):
    print("STOP!")
elif (colour == "YELLOW"):
    print("Prepare to stop")
elif (colour == "GREEN") :
    print("You can go")
else :
    print("Wrong input")
