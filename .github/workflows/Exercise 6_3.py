def letterCounter(word, letter):
    count = 0
    for let in word:
        if let == letter:
            count = count + 1
            
    print(count)

letterCounter(input("Enter the word you wish to count the letters of:"),input("What letter do you want to count?"))
