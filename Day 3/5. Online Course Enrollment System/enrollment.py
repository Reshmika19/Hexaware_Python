class Enrollment:
    def __init__(self, student):
        self.student = student
        self.courses = []
        self.last_enrolled_course = None  

    def enroll_course(self, course):
        if course in self.courses:
            print(f"{self.student.name} is already enrolled in {course.name}.")
        else:
            self.courses.append(course)
            self.last_enrolled_course = course.name
            print(f"Enrolled '{course.name}' for {self.student.name}.")

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"Dropped '{course.name}' from {self.student.name}'s courses.")
        else:
            print(f"{course.name} not found in {self.student.name}'s courses.")

    def calculate_total_credits(self):
        return sum(course.credits for course in self.courses)

    def calculate_total_fees(self):
        return sum(course.get_fee() for course in self.courses)

    def display_courses(self):
        print(f"{self.student.name}'s Courses:")
        if not self.courses:
            print("No courses enrolled.")
        else:
            for c in self.courses:
                print(f"- {c.name} ({c.credits} credits)")
