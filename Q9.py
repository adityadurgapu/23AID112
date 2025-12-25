marks_1 = int(input("Enter your marks in first subject:"))
marks_2 = int(input("Enter your marks in second subject:"))

if (marks_1 >= 50 and marks_2 >= 50):
    print("You passed!" )
    #and is used to satisfy both the conditions.
else:
    print("You need to retake some exams")