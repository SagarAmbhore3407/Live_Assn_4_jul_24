
# example_usage.py

import constants

def calculate_circumference(radius):
    return 2 * constants.PI * radius

def main():
    radius = 5
    circumference = calculate_circumference(radius)
    print(f"The circumference of a circle with radius {radius} is {circumference}")

if __name__ == "__main__":
    main()
