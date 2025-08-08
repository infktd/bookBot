from stats import countWords
from stats import characterCounter
from stats import sortedCharacterCountDictionary
import sys

def getBookText(bookPath):
    with open(bookPath, 'r', encoding='utf-8') as file:
        return file.read()



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        bookText = getBookText(sys.argv[1])
        print("============ BOOKBOT ============")
        print("Analyzing book found at book path:", sys.argv[1])
        print("----------- Word Count ----------")
        print(f"Found {countWords(bookText)} total words")
        print("--------- Character Count -------")
        charCount = characterCounter(bookText)
        sortedCharCount = sortedCharacterCountDictionary(charCount)
        print("Sorted character counts:")
        for char, count in sortedCharCount.items():
            print(f"{char}: {count}")
        print("============= END ===============")

main()
