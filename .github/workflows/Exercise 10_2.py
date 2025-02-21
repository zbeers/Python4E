fname = input("Enter file name: ") #promts user for file name
try: #protects code from invalid file names
    fh = open(fname) #attempts to open file
except:
    print("Please enter valid file name.") #error message
    quit() #stops program in case of bad file name
hist = dict() #creates dictionary
for line in fh: #traverses each line in the file
    if not line.startswith("From "): continue #skips irrelevant lines
    words = line.split() #seperates line into list of words
    time = words[5] #sets the time to a variable which is always the 6th word
    time.split(":") #splits the time using : as the divider
    hour = time[:2] #sets the hour into a variable which goes up to but not include the 3rd character
    hist[hour] = hist.get(hour, 0) + 1 #adds the hour and increments it in the dictionary
lst = list(hist.items()) #creates list
lst.sort() #sorts list since lists are mutable
for key, val in lst: #traverses each tupple in the list
    print(key, val) #prints out the key and value pair