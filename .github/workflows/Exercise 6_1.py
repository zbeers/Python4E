def spellBackwards(word):
    index = -1
    length = len(word)
    while index >= length*-1:
        letter = word[index]
        print(letter)
        index = index - 1

spellBackwards(input("Enter a word:"))