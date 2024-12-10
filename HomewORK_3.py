class Subject:
    def __init__(self, code: str, title: str, credits: float, semester_offered: int):
        # Initialize subject details
        self.code = code
        self.title = title
        self.credits = credits
        self.semester_offered = semester_offered

    def show_subject_info(self):
        # Display subject information
        print(f"Subject Code: {self.code}")
        print(f"Subject Title: {self.title}")
        print(f"Credit Hours: {self.credits}")
        print(f"Offered in Semester: {self.semester_offered}")


# Test block for Subject class
if __name__ == "__main__":
    physics_subject = Subject("PHY101", "Introduction to Physics", 3.5, 1)
    physics_subject.show_subject_info()


class Learner:
    def __init__(self, student_id: str, name: str):
        # Initialize learner details
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = []  # List to store course IDs with grades

    def show_learner_info(self):
        # Display learner information
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")

    def add_course_grade(self, course_code: str, grade: float):
        # Add course grade if within valid range
        if 0 <= grade <= 100:
            self.enrolled_courses.append((course_code, grade))
        else:
            print("Invalid grade! Must be between 0 and 100.")


# Test block for Learner class
if __name__ == "__main__":
    student_keerthi = Learner("56789", "Keerthi Gurram")
    student_keerthi.show_learner_info()
    student_keerthi.add_course_grade("PHY101", 89.5)
    print(f"Grades: {student_keerthi.enrolled_courses}")
