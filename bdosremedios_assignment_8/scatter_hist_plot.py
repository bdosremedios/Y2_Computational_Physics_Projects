import numpy as np #imports numpy as np
import matplotlib.pyplot as plt #imports matlablib.pyplot as plot

#int -> np.array
#makes array of random points of size n using multivariate normal distribution with mean 0,0 and covariance -0.5
def make_rand (n):
    return np.random.multivariate_normal(np.array([0, 0]), (np.array([[1, -0.5],[0.5, -1]])), n)

numpoints = input("Enter your desired number of random points: ") #asks for resired number of points and store in variable
numpoints = int(numpoints) #converts numpoints to int
array = make_rand(numpoints) #calls function on numpoints and stores returned array into array
xdata = array[:,0] #stores x column in xdata
ydata = array[:,1] #stores y column in ydata

plt.scatter(xdata,ydata) #creates scatter plot of data
plt.xlabel("x values") #adds x label
plt.ylabel("y values") #adds y label
plt.title("Scatter plot") #adds title of scatter plot
plt.savefig("bivariate_scatter_plot.pdf") #saves scatter figure in pdf
plt.close() #closes current figure

plt.hist(xdata) #creates historgram of x
plt.xlabel("x values") #adds x label
plt.ylabel("number of points") #adds y label
plt.title("Histogram of x values") #adds title of histogram plot
plt.savefig("bivariate_hist_x_plot.pdf") #saves histogram figure as pdf
plt.close() #closes current figure

plt.hist(ydata) #creates historgram of y
plt.xlabel("y values") #adds x label
plt.ylabel("number of points") #adds y label
plt.title("Histogram of y values") #adds title of histogram plot
plt.savefig("bivariate_hist_y_plot.pdf") #saves histogram figure as pdf
plt.close() #closes current figure

plt.subplot(2,2,1) #creates 2 by 2 plot structure with scatter as 1st (top left)
plt.scatter(xdata,ydata) #creates scatter plot of data
plt.xlabel("x values") #adds x label
plt.ylabel("y values") #adds y label
plt.title("Scatter plot") #adds title of scatter plot
plt.subplot(2,2,2) #creates hist x at 2nd position (top right)
plt.hist(xdata) #creates historgram of x
plt.xlabel("x values") #adds x label
plt.ylabel("number of points") #adds y label
plt.title("Histogram of x values") #adds title of histogram plot
plt.subplot(2,2,3) #creates hist y at 3rd position (bottom left)
plt.hist(ydata) #creates historgram of y
plt.xlabel("y values") #adds x label
plt.ylabel("number of points") #adds y label
plt.title("Histogram of y values") #adds title of histogram plot
plt.subplots_adjust(wspace=0.4,hspace=0.7) #adds spacing in between subplots
plt.savefig("master_plot.pdf") #saves plot as pdf