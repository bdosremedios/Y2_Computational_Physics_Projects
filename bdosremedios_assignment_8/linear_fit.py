import numpy as np #imports numpy abbreviated to np
import scipy.optimize as spo #imports scipy.optimize abbreviated to spo
import matplotlib.pyplot as plt #imports matplotlib.pyplot as abbreviated plt

# float float float -> float
# takes in b x and c and calculates and returns y; y = bx + c
def calcy(x,b,c):
    return b*x+c

examplearray = np.loadtxt("examplearray.txt") #loads array from examplearray.txt
print(examplearray) #prints example array

xdata = examplearray[:,1] #store x col in xdata
ydata = examplearray[:,2] #store y col in ydata
sigma1 = examplearray[:,4] #store yerror in sigma1
linearfit = spo.curve_fit(calcy, xdata, ydata, sigma=sigma1, absolute_sigma=True) #optimizes curve for data in examplearray.txt using calcy giving b and c
parameterserr = np.sqrt(np.diag(linearfit[1])) #calculates and stores error in parameters
parameters = linearfit[0] #stores b and c in parameters

count = range(0,6) #creates range to count over for for loop
linearfity = np.array([0.0,0.0,0.0,0.0,0.0,0.0]) #creats empty array to store values

for i in count: #applies linear fit parameters and function to each x in x storing in linear fity
    y = calcy(xdata[i], parameters[0], parameters[1])
    linearfity[i] = y

plt.errorbar(xdata, ydata, sigma1, fmt="rD") #creates plot line with error bards 
plt.plot(xdata, linearfity, "b-") #creates best fit line
plt.xlabel("x values") #labels x axis
plt.ylabel("y values") #labels y axis
plt.title("Linear fit of examplearray.txt for exercise 1.") # adds title to plot
plt.savefig("linear_fit.pdf") #saves plot as linear_fit.pdf
plt.show(block=False) #shows plot

file=open("linear_fit.txt", "w") #opens file linear_fit.txt to write
file.write("b = {} +/- {}\n".format (parameters[0], parameterserr[0])) #writes parameter b and standard deviation of b in file
file.write("c = {} +/- {}\n".format (parameters[1], parameterserr[1])) #writes parameter c and standard deviation of a in file 
file.close() #closes file
