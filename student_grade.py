students = {
    "Priyanshu": 90,
    "Hari": 85,
    "Rahul": 78
}

name = input("Enter student name: ")

if name in students:
    print("Student already exists!")
    grade = int(input("Enter new grade: "))
    students[name] = grade
    print("Grade updated successfully!")

else:
    grade = int(input("Enter student grade: "))
    students[name] = grade
    print("New student added successfully!")

print("\nAll Student Grades:")

for name, grade in students.items():
    print(name, ":", grade)
