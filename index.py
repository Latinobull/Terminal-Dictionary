import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def getWord(word):
    word = word.lower()
    if word in data:
        return data[word]


word = input("Which word do you want to search? ")

output = getWord(word)

if type(output) == list:

    for item in output:
        print(item)
        print("-------------------------------")
else:
    print(output)