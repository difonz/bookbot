from stats import (
    get_number_of_words,
    get_characters,
    sortDict
)
import sys 

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    bookPath = sys.argv[1]
    text = get_book_text(bookPath)
    wordNum = get_number_of_words(text)
    charDict = get_characters(text)
    sortedCharList = sortDict(charDict)
    printReport(bookPath,wordNum,sortedCharList)
    

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def printReport(bookPath,wordNum, sortedCharList):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {bookPath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordNum} total words")
    print("--------- Character Count -------")
    for item in sortedCharList:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
main()