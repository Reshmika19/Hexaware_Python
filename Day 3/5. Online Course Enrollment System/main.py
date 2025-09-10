from course import Course
from student import Student, PremiumStudent

# Courses
python = Course("Python Programming", "CSE101", 3, 500)
data_science = Course("Data Science 101", "CSE201", 4, 700)
ai = Course("Artificial Intelligence", "CSE301", 5, 900)

# Regular Student
resh = Student("Resh")
resh.enrollment.enroll_course(python)
resh.enrollment.enroll_course(data_science)
resh.enrollment.enroll_course(ai)

resh.enrollment.display_courses()
print(f"{resh.name}'s total credits: {resh.calculate_total_credits()}, Fees: Rs. {resh.calculate_fees()}\n")

# Drop a course
resh.enrollment.drop_course(data_science)
resh.enrollment.display_courses()
print(f"{resh.name}'s total credits: {resh.calculate_total_credits()}, Fees: Rs. {resh.calculate_fees()}\n")

# Premium Student
arjun = PremiumStudent("Arjun")
arjun.enrollment.enroll_course(python)
arjun.enrollment.enroll_course(data_science)
arjun.enrollment.enroll_course(ai)

arjun.enrollment.display_courses()
print(f"{arjun.name}'s total credits: {arjun.calculate_total_credits()}, Fees with discount: Rs. {arjun.calculate_fees()}")
