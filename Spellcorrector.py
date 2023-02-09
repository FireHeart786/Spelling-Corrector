import sys

from spellchecker import SpellChecker

spell = SpellChecker(language='en')

# Open the input file

a= input("enter the location of your file: ")

with open(a, 'r') as file:

    text = file.read()

# Find all spelling mistakes in the text

misspelled_words = spell.unknown(text.split())

# Correct all spelling mistakes

for word in misspelled_words:

    corrected_word = spell.correction(word)

    text = text.replace(word, corrected_word)

# Write the corrected text to the output file

with open('output.txt', 'w') as file:

    file.write(text)

