import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_df = pandas.DataFrame(data)
phonetic_dict = {row.letter: row.code for (index, row) in phonetic_df.iterrows()}

userInput = list(input("Enter the word: ").upper())
result = [f"{phonetic_dict[letter]}" for letter in userInput if letter in phonetic_dict]

print(result)