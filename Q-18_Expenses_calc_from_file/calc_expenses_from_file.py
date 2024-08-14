
# 18. Create a Python script that reads a text file named "expenses.txt" and calculates the total amount spent 
#     on various expenses listed in the file.


def calculate_total_expenses():
    total_expenses = 0.0

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                # Assuming the format is "ExpenseName: $Amount"
                if ':' in line and '$' in line:
                    amount_str = line.split('$')[1].strip()  # Get the amount part after the dollar sign
                    total_expenses += float(amount_str)
    except FileNotFoundError:
        print("The file 'expenses.txt' was not found.")
    except ValueError:
        print("There was a problem with converting an amount to a float.")

    return total_expenses

if __name__ == "__main__":
    total = calculate_total_expenses()
    print(f"Total expenses: ${total:.2f}")
