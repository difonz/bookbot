from stats import get_number_of_words,get_characters


def get_book_text(filePath):
    contents = None
    with open(filePath) as f:
        return f.read()

def main():
    bookPath = 'books/frankenstein.txt'
    text = get_book_text(bookPath)
    print(text)
    numberOfWords =get_number_of_words(text)
    print(f"{numberOfWords} words found in the document")
    
    charactersInText = get_characters(text)
    print(f"{charactersInText}")
    
if __name__ == "__main__":
    main()