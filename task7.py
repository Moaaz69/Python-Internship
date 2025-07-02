# Smart List Analyzer Using Loops and Manual Sorting

def manual_sort(numbers):
    # bubble sort
    n = len(numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

def calculate_stats(numbers):
    # Manual calculations without using sum(), min(), max()
    total = 0
    minimum = numbers[0]
    maximum = numbers[0]
    for num in numbers:
        total += num
        if num < minimum:
            minimum = num
        if num > maximum:
            maximum = num
    average = total / len(numbers) if numbers else 0
    sorted_numbers = manual_sort(numbers[:])  
    return {
        "Sorted": sorted_numbers,
        "Sum": total,
        "Average": round(average, 2),
        "Minimum": minimum,
        "Maximum": maximum
    }

def print_stats(stats):
    # Print each key-value pair with enumerate
    for idx, (key, value) in enumerate(stats.items(), 1):
        print(f"{idx}. {key}: {value}")

def get_user_numbers():
    while True:
        user_input = input("Enter numbers separated by spaces: ")
        try:
            numbers = [float(x) for x in user_input.strip().split()]
            if not numbers:
                print("Please enter at least one number.")
                continue
            return numbers
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces.")


numbers = get_user_numbers()
stats = calculate_stats(numbers)
print("\nCalculated Statistics Summary:")
print_stats(stats)