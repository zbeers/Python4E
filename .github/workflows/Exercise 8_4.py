fname = input("Enter file name: ") #promts user for file name
try: #protects code from invalid file names
    fh = open(fname) #attempts to open file
except:
    print("Please enter valid file name.") #error message
    quit() #stops program in case of bad file name
lst = [] #creates final list to be printed
for line in fh: #goes through each line in the file
    words = line.split() #turns line into a list of words
    for word in words:
        if not word in lst: lst.append(word) #adds word to list not already in list
lst.sort() #sorts list
print(lst) #prints list