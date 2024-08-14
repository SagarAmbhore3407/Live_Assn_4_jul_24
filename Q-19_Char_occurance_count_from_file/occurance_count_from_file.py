
#  19. Create a Python program that reads a text file named "paragraph.txt" and counts the occurrences of 
#      each word in the paragraph, displaying the results in alphabetical order.



import string
from collections import Counter

def count_words(file_path):
    word_count = Counter()

    try:
        with open(file_path, "r") as file:
            for line in file:
                # Remove punctuation and convert to lowercase
                line = line.translate(str.maketrans('', '', string.punctuation)).lower()
                words = line.split()
                word_count.update(words)
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
        return {}

    return dict(word_count)

def display_word_count(word_count):
    for word in sorted(word_count):
        print(f"{word}: {word_count[word]}")

if __name__ == "__main__":
    file_path = "paragraph.txt"
    word_count = count_words(file_path)
    display_word_count(word_count)
