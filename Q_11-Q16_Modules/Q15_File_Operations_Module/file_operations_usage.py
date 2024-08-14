

# file_operations_usage.py

import file_operations

def main():
    file_path = 'sample.txt'
    
    # Write to the file
    file_operations.write_file(file_path, "Sagar Ambhore\n")
    print(f"Written to {file_path}: Sagar Ambhore")
    
    # Append to the file
    file_operations.append_to_file(file_path, "He is a CODEHUSTLER.\n")
    print(f"Appended to {file_path}: He is a CODEHUSTLER.")
    
    # Read from the file
    content = file_operations.read_file(file_path)
    print(f"Content of {file_path}:\n{content}")

if __name__ == "__main__":
    main()
