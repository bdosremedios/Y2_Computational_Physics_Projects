import numpy as np #imports numpy abbreviated as np
import matplotlib.pyplot as plt #imports matplotlib.pyplot as plt

#int float float -> float
#calculates midpoint integration of f(x)=sin(x)e**(-x/2) from x0 to xn
def midpoint(n, x0, xn):
    n = float(n) #makes n float
    midpoint = (xn-x0)/(2*n) #calculates midpoint of each block
    deltax = (xn-x0)/n #calculates deltax or width of each block
    print(deltax)
    list = np.arange(x0+midpoint,xn,deltax) #makes list of all midpoints points of n values from x0 to xn incrementing by one block of deltax width every time
    sum = 0 #makes empty list to store values 
    for x in list: #takes f(x)*deltax of each x in list and adds to sum
        sum = sum + (deltax * (np.sin(x)*np.exp(-x/2)))
    return sum

x0 = -0.5 #sets x0
xn = 2*np.pi #sets xn
n = [10, 20, 100, 200, 400, 800, 1600] #sets values of n needed to be calculated
calcs = [0,0,0,0,0,0,0] #empty list to store calculated values
i = [0,1,2,3,4,5,6] #creates list to count for for loop
for cnt in i:
    temp = midpoint(n[cnt], x0, xn) #calculates midpoint integral of n[cnt] and stores in temp
    calcs[cnt] = temp #stores temp in spot in empty list

plt.plot(n,calcs,"r-",label="midpoint values") #plots calculated midpoint integrals of all n values
plt.xlabel("n values") #labels x axis
plt.ylabel("calculated midpoint integral using n values") #labels y axis
plt.title("Calculated midpoint integral values of $sin(x)e^{-x/2}$ using n values") #adds title to plot

actual = -0.4*np.exp(-xn/2)*(np.sin(xn)+2*np.cos(xn)) - (-0.4*np.exp(-x0/2)*(np.sin(x0)+2*np.cos(x0))) #calculates actual value of indefinite integral
actuallist = [actual,actual,actual,actual,actual,actual,actual] #makes list of actual values
plt.plot(n, actuallist, "b--",label="actual value") #plots line of actual value
plt.legend() #adds legend
plt.savefig("plot_func.pdf") #saves figure in pdf

for cnt in i: #determines at which n value the precision of the integral is within less than 1 percent of the actual value
    if ((actual - 0.01*actual) < calcs[cnt] < (actual + 0.01*actual)):
        onepercentn = n[cnt] #stores first n within 1% in 1percentn
        break #stops the for loop once condition is met
        
f=open("precision.txt","w") #opens text file precision.txt
f.write("Integral precision is less than 1% when n = {}".format (onepercentn)) #writes n value in file
f.close() #closes file