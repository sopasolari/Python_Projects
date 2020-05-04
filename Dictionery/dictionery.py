import json
import difflib
from difflib import SequenceMatcher,get_close_matches

with open("data.json") as reader:
    data = json.load(reader)

def  Word_Meaning(user_input):
    user_input = user_input.lower()
    
    if user_input in data :
        return data[user_input]
    else:
        possibility = get_close_matches(user_input,data.keys())
        if not possibility:
            return "The word not found. Please try another word!"
        else :
            possibility = possibility[0]
            user_ans = input("Did you mean " + possibility + "? pres y for yes or n for no:")
            user_ans = user_ans.lower()
            if user_ans == "y":
                return data[possibility]
            else :
                return "The word not found. Please try another word!"

print(Word_Meaning(input("Enter a word: ")))