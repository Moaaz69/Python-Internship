#Conditional Grading System Using if/elif/else

def  score_to_grade(score):
   
    if not (0 <= score <= 100):
        return "Invalid"
    if score >= 90:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def print_grade_summary(name, score):
    # Prints a formatted grade summary using named parameters.
    grade = score_to_grade(score)
    if grade == "Invalid":
        print(f"Invalid score for student {name}. Please enter a value between 0 and 100.")
    else:
        print(f"Student {name} scored {score} → Grade: {grade}")


print_grade_summary(name="Ali", score=90.5)