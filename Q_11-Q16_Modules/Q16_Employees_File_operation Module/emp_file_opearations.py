
# 16. Write a Python program to create a text file named "employees.txt" and write the details of employees, 
#     including their name, age, and salary, into the file.


# file_operations.py

def write_file(file_path, data):
    """Write data to a file, overwriting any existing content."""
    with open(file_path, 'w') as file:
        file.write(data)
