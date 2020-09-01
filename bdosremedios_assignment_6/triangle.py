#int int int -> printstatement
#takes in three lengths and prints yes if three could form a triangle and no if it can not
def is_triangle(a,b,c):
    if (a > b + c): #checks first stick
        print("No")
    elif (b > a + c): #checks second stick
        print("No")
    elif (c > a + b): #checks third stick
        print("No")
    else:
        print("Yes")

def user_input():
    stick1 = input ("Enter you first stick length here: ") #prompts input of first stick length and stores in stick1
    stick2 = input ("Enter you second stick length here: ") #prompts input of second stick length and stores in stick2
    stick3 = input ("Enter you third stick length here: ") #prompts input of third stick length and stores in stick3
    print("The answer to whether you can form a triangle is: ") #sets up sentence for next line
    is_triangle(stick1,stick2,stick3) #calls is_triangle on given values

user_input()
