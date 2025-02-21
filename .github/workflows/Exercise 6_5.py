str = 'X-DSPAM-Confidence: 0.8475' #given string
str = str.removeprefix('X-DSPAM-Confidence: ') #isolates the float and reassigns it to the same variable
float(str)
print(str)


