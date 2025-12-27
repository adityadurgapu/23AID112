numbers = [12,45,2,98,7,34,21]

#a. Print each number 
print("All numbers in the list:")
for num in numbers:
    print(num)

#b. Print only numbers greater than 30
print("Numbers greater than 30:")
for num in numbers:
    if num > 30:
        print(num)

#c. Count how many numbers are greater than 30
count = 0
for num in numbers:
    if num> 30:
        count += 1
print("The count of numbers greater than 30 are:",count)     