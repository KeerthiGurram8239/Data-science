
# Function to convert letter grades to GPA points
def get_gpa_points(letter_grade):
    letter_grade = letter_grade.upper()
    gpa_points = {
        'A': 4.0, 'A-': 3.7, 'B+': 3.3, 'B': 3.0,
        'B-': 2.7, 'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'F': 0.0
    }
    return gpa_points.get(letter_grade, 0.0)

# Main function to compute GPA
def run_gpa_calculator():
    courses_count = int(input("Enter the total number of courses (1-7): "))
    
    # Validate the number of courses
    if courses_count < 1 or courses_count > 7:
        print("Please enter a number between 1 and 7 for the courses.")
        return

    overall_points = 0.0
    overall_credits = 0

    for course in range(courses_count):
        grade = input(f"Enter the grade for course {course + 1}: ")
        
        # Loop to ensure valid credit input
        while True:
            try:
                course_credits = int(input(f"Enter the credits for course {course + 1} (1-5): "))
                if 1 <= course_credits <= 5:
                    break  # Exit loop for valid input
                else:
                    print("Credits should be a whole number between 1 and 5.")
            except ValueError:
                print("Invalid input. Please enter a valid whole number for credits.")

        # Add to total points and credits
        overall_points += get_gpa_points(grade) * course_credits
        overall_credits += course_credits

    # Calculate the GPA
    final_gpa = overall_points / overall_credits
    print(f"Your calculated GPA is: {final_gpa:.2f}")

# Trigger the main function
if __name__ == "__main__":
    run_gpa_calculator()
