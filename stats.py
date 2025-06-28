def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    charDict = {}
    for c in text:
        lowered = c.lower()
        if lowered in charDict:
            charDict[lowered] +=1
        else:
            charDict[lowered]=1
    return charDict


def sort_on(d):
    return d["num"]

def sortDict(charDict):
    sortedList = []
    for char in charDict:
        sortedList.append({"char": char, "num": charDict[char]})
    sortedList.sort(reverse=True,key=sort_on)
    return sortedList   
    