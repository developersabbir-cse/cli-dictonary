from difflib import get_close_matches
import json
data = json.load(open("./data.json"))

def translator(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w,data.keys()))>0:
        yn = input("Did you mean %s instead, Enter Y if yes, or N if no: " % get_close_matches(w,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please Check again!"
        else:
            return "We didn't understand your entry!"
    else:
        return "The word doesn't exist. Please Check again!"

word = input("Enter word: ")

output = translator(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
