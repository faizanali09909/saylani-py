print("=== Simple Grade Calculator ===")

name = input("Enter student name: ")
num_subjects = int(input("Enter number of subjects: "))

total = 0

for i in range(num_subjects):
    marks = float(input(f"Enter marks for subject {i + 1} (out of 100): "))
    total = total + marks

average = total / num_subjects

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n--- Result ---")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Grade:", grade)