# GPA Calculator Using Functions


def calculate_gpa(grades, total_points=4.0):

    if not grades:
        return 0.0
    gpa = sum(grades) / len(grades)
    # Ensure GPA does not exceed the total_points scale
    gpa = min(gpa, total_points)
    return round(gpa, 2)

# Example usage
grades_list = [3.5, 3.7, 4.0, 3.2, 3.8]

# Function call using named arguments
gpa = calculate_gpa(grades=grades_list, total_points=4.0)

# Displaying results
print(f"Grades: {grades_list}")
print(f"GPA (on 4.0 scale): {gpa}")