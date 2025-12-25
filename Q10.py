Temp = float(input("Enter the temperature in celsius:"))
Fahrenheit = (Temp*9/5) + 32

print("The temperature in Fahrenheit is:",Fahrenheit)

if (Temp < 0 ):
    print("Very cold! Wear thick jacket")
elif (0 <= Temp <=15 ):
    print("Cold. Wear jacket")
elif (16 <= Temp  <= 25):
    print("Nice weather")
else :
    print("Hot! Stay hydrated")