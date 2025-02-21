fname = input("Enter file name: ") #promts user for file name
try: #protects code from invalid file names
    fh = open(fname) #attempts to open file
except:
    print("Please enter valid file name.") #error message
    quit() #stops program in case of bad file name
count = 0 #
for line in fh: #for each line in the file
    if not line.startswith("From "): continue #skips irrelevant lines
    lst = line.split() #makes lines into list
    print(lst[1]) #prints the email which is always the second word
    count = count + 1 #iterates the count
print("There were", count, "lines in the file with From as the first word") #count message