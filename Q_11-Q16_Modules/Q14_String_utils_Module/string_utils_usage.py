

# String_utils_usage.py

# example_usage.py

import string_utils

def main():
    sample_string = "Hello World"
    
    print(f"Original: {sample_string}")
    print(f"Reversed: {string_utils.reverse_string(sample_string)}")
    print(f"Capitalized: {string_utils.capitalize_string(sample_string)}")
    print(f"Uppercase: {string_utils.to_uppercase(sample_string)}")
    print(f"Lowercase: {string_utils.to_lowercase(sample_string)}")
    
    palindrome_test = "A man, a plan, a canal, Panama"
    print(f"Is palindrome: {palindrome_test} -> {string_utils.is_palindrome(palindrome_test)}")

if __name__ == "__main__":
    main()
