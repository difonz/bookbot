def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_characters(text):
    charDict = {}
    for letter in text:
        lowerChar = letter.lower()
        charDict[lowerChar] = charDict.get(lowerChar,0)+1
    return charDict