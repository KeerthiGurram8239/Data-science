# Student Class Definition

class Student:
    def __init__(self, student_number: str, student_name: str):
        # Initialize student details
        self.student_number = student_number
        self.student_name = student_name
        self.course_grades = []  # List to store course and grade tuples

    def display_student_info(self):
        # Print the student ID and name
        print(f"Student Number: {self.student_number}")
        print(f"Student Name: {self.student_name}")

    def record_course_grade(self, course_code: str, grade: float):
        # Add course and grade if the grade is valid
        if 0 <= grade <= 100:
            self.course_grades.append((course_code, grade))
        else:
            print("Invalid grade. It must be between 0 and 100.")


# Test block for Student class
if __name__ == "__main__":
    test_student = Student("98765", "Keerthi Gurram")
    test_student.display_student_info()
    test_student.record_course_grade("MATH201", 88.0)
    print(f"Enrolled Courses and Grades: {test_student.course_grades}")
