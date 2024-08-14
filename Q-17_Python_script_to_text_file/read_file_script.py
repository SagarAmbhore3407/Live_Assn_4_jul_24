
#  17. Develop a Python script that opens an existing text file named "inventory.txt" in read mode and displays 
#      the contents of the file line by line.


def display_inventory():
    try:
        with open("inventory.txt", "r") as file:
            for line in file:
                print(line.strip())  # strip() removes any leading/trailing whitespace including the newline character
    except FileNotFoundError:
        print("The file 'inventory.txt' was not found.")

if __name__ == "__main__":
    display_inventory()

