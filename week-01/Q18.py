Secret_num = 7
num = (int(input("Guess the secret number:")))

while num != Secret_num:
    if num < Secret_num:
        print("Too low")
    elif num > Secret_num:
        print("Too high")
    num = (int(input("Guess the secret number:")))

print("The guess is correct")  
