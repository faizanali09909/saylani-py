# Task 1

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# Task 2
marks = int(input("Enter your marks: "))

if marks < 40:
    print("Fail")
elif marks >= 40 and marks < 60:
    print("Pass")
elif marks >= 60 and marks < 70:
    print("C Grade")
elif marks >= 70 and marks < 80:
    print("B Grade")
elif marks >= 80 and marks < 90:
    print("A Grade")
elif marks == 100:
    print("Perfect Score")
elif marks >= 90 and marks < 100:
    print("A+ Grade")
elif marks > 100:
    print("Don't Suck Up To The Teacher")
