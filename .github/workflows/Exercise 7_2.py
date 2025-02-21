# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ") #promts user for file name
try: #makes sure file is valid
    fh = open(fname) #opens file
except:
    print("Enter valid file name") #Error message
    quit() #terminates when error encountered
total = 0.0 #sets total to a float
lines = 0 #itteration variable to find the number of lines
for line in fh: #for each line in the file,
    if not line.startswith("X-DSPAM-Confidence:"): #skips non-relevant lines
        continue
    if line.startswith("X-DSPAM-Confidence:"): #if line is relevant,
        numStart = line.find('0') #finds where in the line the number starts
        con = float(line[numStart:]) #Stores floated string into the variable
        total = total + con #adds the float to the total
        lines = lines + 1 #counts number of lines
avg = total/lines #calculates average
print("Average spam confidence:", avg)
