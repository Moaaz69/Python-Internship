# Student Marks Reader with Exception Handling

def read_student_marks():
    skipped = 0
    student_marks = {}
    while True:
        file_path = input("Enter the path to the marks file: ").strip()
        try:
            with open(file_path, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        name, mark = line.split(",", 1)
                        name = name.strip()
                        mark = mark.strip()
                        if not name or not mark:
                            skipped += 1
                            continue
                        mark_int = int(mark)
                        student_marks[name] = mark_int
                    except ValueError:
                        skipped += 1
                        continue
            break
        except FileNotFoundError:
            print("File not found. Please try again.")
    return student_marks, skipped

def print_marks_and_average(student_marks, skipped):
    if not student_marks:
        print("No valid student marks found.")
        return
    print("\nStudent Marks:")
    total = 0
    count = 0
    for name, mark in student_marks.items():
        print(f"{name}: {mark}")
        total += mark
        count += 1
    try:
        average = total / count
        print(f"\nAverage Mark: {round(average, 2)}")
    except ZeroDivisionError:
        print("\nCannot calculate average (no valid marks).")
    print(f"Skipped entries: {skipped}")


student_marks, skipped = read_student_marks()
print_marks_and_average(student_marks, skipped)