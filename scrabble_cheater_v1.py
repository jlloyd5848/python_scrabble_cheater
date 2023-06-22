# Author: Joshua Lloyd

# Title : Scrabble Cheater Program

from itertools import permutations
from collections import Counter
import tkinter as tk

# Function to calculate the score of a word
def calculate_score(word):
    letter_scores = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8,
        'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1,
        'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }
    score = 0
    for letter in word:
        score += letter_scores.get(letter, 0)
    return score

# Function to find all possible words from a given set of letters
def find_possible_words(letters):
    possible_words = set()
    for length in range(1, len(letters) + 1):
        perms = permutations(letters, length)
        for perm in perms:
            word = ''.join(perm)
            possible_words.add(word)
    return possible_words

# Function to check if a word can be formed from a set of letters
def can_form_word(word, letters):
    word_count = Counter(word)
    letters_count = Counter(letters)
    for letter, count in word_count.items():
        if count > letters_count.get(letter, 0):
            return False
    return True

# Function to find the best word and its score from a given set of letters
def find_best_word(letters, word_list):
    possible_words = find_possible_words(letters)
    best_word = ''
    best_score = 0
    for word in possible_words:
        if word in word_list and can_form_word(word, letters):
            score = calculate_score(word)
            if score > best_score:
                best_word = word
                best_score = score
    return best_word, best_score

# Function to handle the button click event
def find_word():
    letters = entry.get().lower()
    best_word, best_score = find_best_word(letters, word_list)
    if best_word:
        result_label.config(text=f"The best word you can form is '{best_word}' with a score of {best_score}.")
    else:
        result_label.config(text="No valid words can be formed.")

# Load word list from a text file
def load_word_list(file_path):
    with open(file_path, 'r') as file:
        word_list = file.read().splitlines()
    return word_list

# Load the word list file
word_list = load_word_list('word_list.txt')  # Replace 'word_list.txt' with the path to your word list file

# Create the main window
window = tk.Tk()
window.title("Scrabble Cheater")

# Create the input label and entry
input_label = tk.Label(window, text="Enter your letters:")
input_label.pack()
entry = tk.Entry(window)
entry.pack()

# Create the button
button = tk.Button(window, text="Find Word", command=find_word)
button.pack()

# Create the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()
