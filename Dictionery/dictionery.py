import json

with open("data.json") as reader:
    data = json.load(reader)

def  Word_Meaning(user_input):
    if user_input in data :
        return data[user_input]
    else :
        return "The word not found. Please try again!"

print(Word_Meaning(input("Enter a word: ")))