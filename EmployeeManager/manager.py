from employee import Employee

class EmployeeManager:
    def __init__(self, data_file="employee_data.txt"):
        self.data_file = data_file
        self.employees = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.data_file, "r") as f:
                for line in f:
                    if line.strip():
                        self.employees.append(Employee.from_csv(line))
        except FileNotFoundError:
            pass

    def save_to_file(self):
        with open(self.data_file, "w") as f:
            for emp in self.employees:
                f.write(emp.to_csv() + "\n")

    def add_employee(self, name, department, salary, joining_year):
        self.employees.append(Employee(name, department, salary, joining_year))

    def list_employees(self):
        for emp in self.employees:
            emp.display()

    def search_employee(self, term):
        results = list(filter(lambda e: term.lower() in e.name.lower() or term.lower() in e.department.lower(), self.employees))
        for emp in results:
            emp.display()

    def sort_by_salary(self, desc=False):
        self.employees.sort(key=lambda e: e.salary, reverse=desc)

    def generate_report(self, report_file="employee_report.txt"):
        with open(report_file, "w") as f:
            f.write("Employee Report\n")
            f.write("====================\n")
            for emp in self.employees:
                f.write(f"{emp.name} | {emp.department} | {emp.salary} | {emp.joining_year}\n")
            if self.employees:
                avg_salary = sum(e.salary for e in self.employees) / len(self.employees)
                f.write(f"\nTotal Employees: {len(self.employees)}\n")
                f.write(f"Average Salary: {avg_salary:.2f}\n")
            else:
                f.write("\nNo employees in the system.\n")