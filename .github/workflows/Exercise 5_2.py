largest = None #creates variable for maximum to use at the end
smallest = None #creates variable for minimum to use at the end
num_list = [] #creates a list to store values from user input for later
while True:
    num = input("Enter a number: ") #promts user for numerical input
    if num == "done": #checks for done input to break
        largest = max(num_list) #uses max function to find the maximum from num_list
        smallest = min(num_list) #uses min function to find the minimum from num_list
        break #breaks infinite loop
    try:
        num = int(num) #attempts to turn user input into an integer
        num_list.append(num) #stores user input in a list to use for later
    
    except:
        print("Invalid input") #error message
        continue #has us go back to the top of infinite loop instead of crashing out

print("Maximum is", largest) #prints maximum
print("Minimum is", smallest) #prints minimum