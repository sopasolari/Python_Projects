import json #Import json and get_close_matches from difflib header
from difflib import get_close_matches 

with open("data.json") as reader: #Open file data.json
    data = json.load(reader) #we store all the json file to variable data

def  Word_Meaning(user_input): #Function to return the meaning of the word
    user_input = user_input.lower()#Make the user input word lowercase
    
    if user_input in data : # Check if the user input value it is in the dictionery
        return data[user_input] #return the meaning of the word
    elif user_input.capitalize() in data :#Check for the capitals for example Paris
        return data[user_input.capitalize()]
    elif user_input.upper() in data: #Another condition to search word like USA,NATO
        return data[user_input.upper()]
    else:
        possibility = get_close_matches(user_input,data.keys(),cutoff=0.8) #Assign in variable the possibility word
        if not possibility: #Check if the dict is empty!
            return {"The word not found. Please try another word!"}
        else :
            possibility = possibility[0] #Renew the value possibility and we take the first word from dictonery
            user_ans = input("Did you mean " + possibility + " instead? Enter y for yes or n for no:") #Ask the user if is correct word
            user_ans = user_ans.lower() #Make the answer lower to check with y or n
            if user_ans == "y":
                return data[possibility]
            elif user_ans == "n":
                return {"The word not found. Please double check!"} #If user dont press n/N we return this message
            else :
                return {"We don't understand your choice!"} #If user dont press y/Y or n/N we return this message

print(*Word_Meaning(input("Enter a word: ")),sep='\n') #Ask the user to enter a word and call the function Word_Meaning