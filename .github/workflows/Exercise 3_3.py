score = input("Enter Score: ") #Promts user imput
try:
    score = float(score)
    if score >= 0.9: #Checks for A
        letter = "A" #Assigns letter
    elif score >= 0.8: #Checks for B
        letter = "B" #Assigns letter
    elif score >= 0.7: #Checks for C
        letter = "C" #Assigns letter
    elif score >= 0.6: #Checks for D
        letter = "D" #Assigns letter
    elif score < 0.6: #Checks for F
        if score > 0: #Checks for valid score
            letter = "F" #Assigns letter
    else: #If score is negative
        print("Please enter a valid float in range!")
    print(letter) #Prints Score
except:
    print("Please enter a float!")