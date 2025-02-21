fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip() #gets rid of new line characters
    if not line.startswith('From: '):
        continue #Skips over lines without designated prefix
    if line.startswith('From: '):
        print(line) #prints email addresses
    