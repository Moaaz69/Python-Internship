from manager import EmployeeManager
from utils import get_input

def main():
    manager = EmployeeManager()
    while True:
        print("\nEmployee Manager Menu:")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Search by Name/Dept")
        print("4. Sort by Salary")
        print("5. Generate Report")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            name = get_input("Name: ")
            dept = get_input("Department: ")
            salary = get_input("Salary: ", float)
            year = get_input("Joining Year: ", int)
            manager.add_employee(name, dept, salary, year)
            print("Employee added.")
        elif choice == "2":
            manager.list_employees()
        elif choice == "3":
            term = get_input("Enter name or department to search: ")
            manager.search_employee(term)
        elif choice == "4":
            desc = input("Sort descending? (y/n): ").strip().lower() == "y"
            manager.sort_by_salary(desc)
            print("Employees sorted by salary.")
        elif choice == "5":
            manager.generate_report()
            print("Report generated as employee_report.txt")
        elif choice == "6":
            manager.save_to_file()
            print("Data saved. Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()