# list -> tuple
# takes a list and returns a tuple of the first and last element
def ends(t):
    if (t == []): #returns 0th element and last element in list unless list is empty in which case it returns an empty tuple
        return ()
    else:
        return (t[0],t[-1])

usrinput = input("How many items would you like to put in the list?: ") # Asks user to input the length of the list they want and stores in usrinput
usrinput = int(usrinput) #makes usrinput an int
list = [] #creates empty list
while(usrinput > 0): #makes list go from 0 to userinput - 1 giving a list of size usrinput
    #also does not run if negative number is given simply treating a negative number as an empty array
    list = [usrinput - 1] + list
    usrinput = usrinput - 1

tuple = ends(list) #calls ends with desired list and stores in tuple

if (tuple == ()): #checks if gave empty array
    print("List was empty")
else: #if not prints first and second elements
    print("The first element is: {}, and the second element is {}". format(tuple[0],tuple[1]))
