"""
3: Utilities Package
A data analytics team often needs to clean text, perform math, and handle files.
Instead of writing these functions every time, they create a utilities package.

Modules:
- string_ops.py → Remove punctuation, count vowels, lowercase.
- math_ops.py   → Mean, median, standard deviation.
- file_ops.py   → Read, write, search in files.
"""

from utilities import (
    remove_punctuation, count_vowels, to_lowercase,
    mean, median, standard_deviation,
    read_file, write_file, search_in_file
)

def main():
    # String operations
    text = "Hello, World! Python is great!!!"
    print("Original text:", text)
    print("No punctuation:", remove_punctuation(text))
    print("Vowel count:", count_vowels(text))
    print("Lowercase:", to_lowercase(text))

    # Math operations
    numbers = [10, 20, 30, 40, 50]
    print("\nNumbers:", numbers)
    print("Mean:", mean(numbers))
    print("Median:", median(numbers))
    print("Standard Deviation:", standard_deviation(numbers))

    # File operations
    write_file("sample.txt", "Python is fun.\nData Analytics is powerful.\nWe love Python.")
    print("\nFile written successfully.")
    print("File contents:\n", read_file("sample.txt"))
    print("Search 'Python':", search_in_file("sample.txt", "Python"))

if __name__ == "__main__":
    main()
