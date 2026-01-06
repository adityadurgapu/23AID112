import random

num =[random.randint(1,101)
      for i in range(8)]
print("The random numbers are:",num)

biggest = num[0]
smallest = num[0]

for x in num:
    if x > biggest:
        biggest = x
    if x < smallest:
        smallest = x
print("The biggest number is:",biggest)
print("The smallest number is:",smallest)
