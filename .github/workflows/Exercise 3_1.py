# This first line is provided for you
try
    hrs = float (input("Enter Hours:")) #Defines number of hours worked and makes it a float
    rte = float (input("Enter Rate:"))  #Defines hourly rate and makes it a float
    if hrs > 40 #checks for bonus if so then calculates and prints
        rte = rte*1.5 #Calculates bonus rate
        pay = hrs*rte #Calculates pay from user entered rate and hours
        print("Pay: " + str(pay)) #prints result
    else #if no bonus calculates and prints 
        pay = hrs*rte #Calculates pay from user entered rate and hours
        print("Pay: " + str(pay))
except #Makes sure a numerical value is entered
    print("Please enter a numerical value!")