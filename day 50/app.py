import json
from difflib import get_close_matches
data = json.load(open("python-projects/English Thesaurus/data.json"))

def translate(word):
    if word in data:
        return data[word]

    elif len(get_close_matches(word,data.keys())) > 0:
        ans = input("Did you mean %s instead ? Enter Y if yes, or N if no: " % get_close_matches(word,data.keys())[0])

        if ans == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif ans == "N":
            return "The word doesn't exist. Please double check it"
        else:
            return "We didn't understand your entry"

    else:
        return "The word doesn't exist. Please double check it"

word = str(input("Enter your word: "))
word = word.lower()

result = translate(word)

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)