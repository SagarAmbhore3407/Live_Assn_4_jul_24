

#  14. Implement a Python module named string_utils.py containing functions for string manipulation, such as 
#  reversing and capitalizing strings.


# string_utils.py

# string_utils.py

def reverse_string(s):
    """Return the reversed version of the input string."""
    return s[::-1]

def capitalize_string(s):
    """Return the input string with the first letter of each word capitalized."""
    return s.title()

def to_uppercase(s):
    """Return the input string converted to uppercase."""
    return s.upper()

def to_lowercase(s):
    """Return the input string converted to lowercase."""
    return s.lower()

def is_palindrome(s):
    """Check if the input string is a palindrome."""
    cleaned = ''.join(filter(str.isalnum, s)).lower()  # Remove non-alphanumeric characters and convert to lowercase
    return cleaned == cleaned[::-1]
