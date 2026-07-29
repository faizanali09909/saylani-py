marks = int(input("Enter your marks: "))

if marks > 100:
    print("Wrong marks!")
elif marks >= 90:
    print("You have passed with distinction!")
elif marks >= 60:
    print("You have passed!")
else:
    print("You have failed!")