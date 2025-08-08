def countWords(bookText):
    words = bookText.split()
    return len(words)

def characterCounter(text):
    counts = {}
    for char in text.lower():
        if char in 'abcdefghijklmnopqrstuvwxyz':
            counts[char] = counts.get(char, 0) + 1
    return counts

def sortedCharacterCountDictionary(d):
    # Sort the dictionary by value (count) in descending order
    return dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
