import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def getWord(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input(
            "Did you mean %s instead? Enter Y if yes, or N if no:"
            % get_close_matches(word, data.keys())[0]
        )
        if yn == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "Sorry we did not understand your entry"
    else:
        return word + " does not exist. Please check your spelling."


word = input("Which word do you want to search? ")

output = getWord(word)

if type(output) == list:

    for item in output:
        print(item)
        print("-------------------------------")
else:
    print(output)