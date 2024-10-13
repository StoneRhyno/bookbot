import os

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    char_counts = {}
    for char in text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

# Construct the path to the file in the 'books' subfolder
file_path = os.path.join('books', 'frankenstein.txt')

with open(file_path, 'r') as file:
    content = file.read()
    print(content)

word_count = count_words(content)
print(f"The number of words in the file is: {word_count}")

character_counts = count_characters(content)
print("Character counts:")
for char, count in character_counts.items():
    print(f"'{char}': {count}")
