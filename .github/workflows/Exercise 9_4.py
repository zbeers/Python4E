fname = input("Enter file name: ") #promts user for file name
try: #protects code from invalid file names
    handle = open(fname) #attempts to open file
except:
    print("Please enter valid file name.") #error message
    quit() #stops program in case of bad file name
hist = dict()
for line in handle: #itterates through each line in the file
    if not line.startswith("From "): continue #skips irrelavant lines
    words = line.split() #makes the line into a list of words
    email = words[1] #saves the email which is always the second word into a variable
    hist[email] = hist.get(email, 0) + 1 #creates a dictionary item for the email and sets the value
sndr = None #email variable
count = None #repetition variable
for word, val in list(hist.items()): #traverses each key and value in the dictionary
    if count is None or val > count: #checks for if there is no largest amount or if the current amount is larger than the last
        sndr = word #changes email to current largest
        count = val #changes count to corresponding key value
print(sndr, count) #prints result