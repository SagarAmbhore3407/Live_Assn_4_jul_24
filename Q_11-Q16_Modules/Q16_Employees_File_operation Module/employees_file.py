
# 16. Write a Python program to create a text file named "employees.txt" and write the details of employees, 
#    including their name, age, and salary, into the file.


# employees_file.py

import emp_file_opearations

def create_employee_file(file_path, employees):
    """Write the details of employees to a file."""
    with open(file_path, 'w') as file:
        for employee in employees:
            file.write(f"Name: {employee['name']}, Age: {employee['age']}, Salary: {employee['salary']}\n")

def main():
    file_path = 'employees.txt'
    
    # Sample employee data
    employees = [
        {"name": "akash jadhav", "age": 30, "salary": 50000},
        {"name": "Dominic Torrato", "age": 25, "salary": 60000},
        {"name": "Amit jaiswal", "age": 35, "salary": 70000},
        {"name": "Nishant jarare", "age": 40, "salary": 80000}
    ]
    
    # Create the employee file
    create_employee_file(file_path, employees)
    print(f"Employee details have been written to {file_path}")

if __name__ == "__main__":
    main()
