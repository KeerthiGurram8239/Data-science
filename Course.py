# Course Class Definition

class Course:
    def __init__(self, course_code: str, course_title: str, credit_hours: float, semester: int):
        # Initialize the course details
        self.course_code = course_code
        self.course_title = course_title
        self.credit_hours = credit_hours
        self.semester = semester

    def display_course_info(self):
        # Display all course attributes
        print(f"Course Code: {self.course_code}")
        print(f"Course Title: {self.course_title}")
        print(f"Credits: {self.credit_hours}")
        print(f"Semester Offered: {self.semester}")


# Test block for Course class
if __name__ == "__main__":
    test_course = Course("MATH201", "Calculus I", 3.0, 2)
    test_course.display_course_info()
