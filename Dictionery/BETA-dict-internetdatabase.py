import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word=input("Enter the word: ")
sqlFormula = "SELECT * FROM Dictionary"

cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[0])
else:
    cursor.execute(sqlFormula)
    possibility = cursor.fetchall()
    possibility = dict(possibility)
    cor_word = get_close_matches(word,possibility,cutoff=0.8)
    if cor_word:
        answer = input("Did you mean " + cor_word[0] +"? Enter y for yes or n for no: ")
        answer = answer.lower()
        if answer == "y" or answer == "yes":
            print(possibility[cor_word[0]])
        elif answer == "n" or answer == "no" :
            print("No word found!")
        else:
            print("We dont understand your choice!")
    else:
        print("No word found!")