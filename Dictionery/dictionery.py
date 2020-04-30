import json

with open("data.json") as reader:
    data = json.load(reader)

def  Word_Meaning(user_input):
    return data[user_input]

print(Word_Meaning(input("Enter a word: ")))