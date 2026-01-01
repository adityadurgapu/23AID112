def check_password(password):
    length=len(password) >=8

    uppercase = False
    lowercase = False
    digit = False
    special = False

    for char in password:
        if char.isupper():
            uppercase = True
        elif char.islower():
            lowercase = True
        elif char.isdigit():
            digit = True
        else:
            special = True
    
    score = 0
    if length:
        score += 1
    if uppercase:
        score += 1
    if digit:
        score += 1
    if lowercase:
        score += 1
    if special:
        score += 1 

    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print("\nLength is more than:",length)
    print("Uppercase letter:",uppercase)
    print("Lowercase letter:",lowercase)
    print("Digit:",digit)
    print("Special character:",strength)

password = input("Enter your password:")
check_password(password)