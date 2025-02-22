import re #gives us regular expression methods
fname = input("Enter file name: ") #promts user for file name
try: #protects code from invalid file names
    fh = open(fname) #attempts to open file
except:
    print("Please enter valid file name.") #error message
    quit() #stops program in case of bad file name
nums = list() #creates list
total = 0 #creates variable to store the total
for line in fh: #traverses each line in the file
    line = line.rstrip() #turns line into list of words
    if not re.findall('[0-9]+', line): continue #skips lines without numbers
    nums.append(re.findall('[0-9]+', line)) #adds numbers to list
for items in nums: #traverses each list of numbers in nums
    for num in items: #traverses each number in the sublists
        total = total + int(num) #increments the total through each number in the file
print("The total from this file is", total) #prints total