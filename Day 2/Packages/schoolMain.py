"""
Scenario 4: School Package
A school management system needs to keep track of students, teachers, and results.

Modules:
- students.py → Add students, view student list.
- teachers.py → Assign subjects, view teacher info.
- results.py  → Calculate grades from marks.

Implementation Idea:
When generating a report card, the program pulls student info from school.students,
teacher details from school.teachers, and calculates grades using school.results.
"""

from school import add_student, view_students, assign_subject, view_teacher, calculate_grade

def main():
    # Add students
    add_student("Reshmika", 101)
    add_student("Nisha", 102)

    # Assign teachers
    assign_subject("Mr. Ravi", "Mathematics")
    assign_subject("Ms. Priya", "Science")

    # View students
    print("Students List:")
    for s in view_students():
        print(f"Roll No: {s['roll_no']}, Name: {s['name']}")

    # View teachers
    print("\nTeachers List:")
    for t in view_teacher():
        print(f"Teacher: {t['name']}, Subject: {t['subject']}")

    # Generate report card
    print("\nReport Card:")
    marks = {"Reshmika": 92, "Arun": 68}
    for name, mark in marks.items():
        print(f"Student: {name}, Marks: {mark}, Grade: {calculate_grade(mark)}")

if __name__ == "__main__":
    main()
