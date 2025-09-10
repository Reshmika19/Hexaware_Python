import string

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

def to_lowercase(text):
    return text.lower()
