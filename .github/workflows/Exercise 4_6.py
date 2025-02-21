def computePay(hrs, rte):
# This first line is provided for you
    try: #Main code
        hrs = float (hrs)  #Floats hours
        rte = float (rte)  #Floats rate
        if hrs > 40: #Checks for bonus if so then calculates and prints
            hrs = hrs-40 #Calculates how many hours get the bonus rate
            bns = hrs*(rte*1.5) #Calculates bonus
            pay = (40*rte)+bns #Calculates pay from user entered rate and hours
        else: #If no bonus calculates and prints
            pay = hrs*rte #Calculates pay from user entered rate and hours
        return "Pay: ", pay
    except: #Prints statement if non-numerical argument is entered
        print("Please enter a numerical value!")
        
computePay(input("Enter hours: "), input("Enter rate: ")) #Runs compute pay with input as arguments for the function
