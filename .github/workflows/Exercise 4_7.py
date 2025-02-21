def computeGrade(score):
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
        elif score < 0.6 and score > 0: #Checks for F and if score is a positive number
            letter = "F" #Assigns letter
        else: #If score is negative
            print("Please enter a positive float!")
    except:
        print("Please enter a float!")
    return print(letter)
computeGrade(input("Enter Score: "))