# Use words.txt as the file name
fname = input("Enter file name: ")
try: #makes sure file is real
    fh = open(fname) #opens file for reading

except: #if invalid file name
    print("Please enter a valid file name")
    quit()

for line in fh: #for each line in the file,
    line = line.upper() #turns the line into uppercase
    line = line.rstrip() #gets rid of whitespace
    print(line) #prints line