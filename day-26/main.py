import pandas as pd

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_phenonetic_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_phenonetic_dic = {row.letter: row.code for (index, row) in nato_phenonetic_data.iterrows()}
# print(nato_phenonetic_dic)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input('Enter a word: ')
user_word_letters = [letter.upper() for letter in user_word]
user_word_phonetic_list = [word for i in user_word_letters for (letter, word) in nato_phenonetic_dic.items() if letter == i]

print(user_word)
print(user_word_letters)
print(user_word_phonetic_list)