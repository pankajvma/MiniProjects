import pandas as pd

df = pd.read_csv('nato_phonetic_alphabet.csv')

name = input("Enter your name: ")
print("\nHere are the NATO alphabets corresponding to exact letter in your name.\n")

phonetic_dictionary = {row.letter:row.code for (index, row) in df.iterrows()}


phonetic_words = [f"{letter}: {phonetic_dictionary[letter]}" for letter in name.upper()]

for word in phonetic_words:
    print(word)