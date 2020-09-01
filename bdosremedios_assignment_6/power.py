#int int -> boolean
#takes ints a and b and produces true if a is a power of b
def is_power(a,b):
    if ((a % b) != 0): #checks if ever gives remainder meaning not a power of b 
        return False
    elif (a == b): #checks if a is b after division 
        return True
    else:
        return is_power(a/b, b) #recurs is_power using newvalue of a divided by b

numa = input("Enter number desired to be tested here: ")
#takes value of desired tested number and store in a
numb = input("Enter number desiring first number to be tested by: ")
#takes value of desired number the first number is to be tested by
numa = int(numa) #converts numa to int
numb = int(numb) #converts numb to int
if (is_power(numa,numb)): #calls function onto given values
    print("{} is a power of {}".format (numa, numb)) #prints if is power
else:
    print("{} is not a power of {}".format (numa, numb)) #prints if isn't power

