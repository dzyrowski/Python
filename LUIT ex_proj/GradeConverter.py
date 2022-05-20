#This script will convert numerical grade to a letter grade

grade = (float(input("Enter your numerical grade: ")))

if grade >= 90 and grade<= 100:
    print("You have an A")
elif grade < 90 and grade >= 80:
    print("You have a B")
elif grade < 80 and grade >= 70:
    print("You have a C")
elif grade < 70 and grade >= 60:
    print("You have a D")
else:
    print("You have a F")
