import numpy as np #imports numpy as abbreviated np
array = np.random.random((1, 100)) #creates random array of size 100 on interval [0,1)

#Q1
arraymean = np.sum(array) / 100 #calculates the mean value of the array
print("A1: The mean value is: " + str(arraymean)) #prints mean value
#The mean value is around 0.5 which makes sense as the numbers would tend to be in equal amounts nearly above and below

#Q2
var = 1 / 99 * np.sum((array - arraymean) * (array - arraymean)) #calculates variance of random array
print("A2.1: The variance is: " + str(var)) #prints var
stdev = np.sqrt(var) #calculates standard deviation
print("A2.2: The standard deviation is: " + str(stdev)) #prints stdev
#So far the values of both seem fairly reasonable

#Q3
npmean = np.mean(array) #calculates mean using built in np func
print("A3.1: The np calculated mean is: " + str(npmean)) #prints npmean
npvar = np.var(array) #calculates variance using built in np func
print("A3.2: The np calculated variance is: " + str(npvar)) #prints npvar
npstd = np.std(array) #calculates stdeviation using built in np func
print("A3.3: The np calculated standard deviation is: " + str(npstd)) #prints npstd
#The results do not match what I got earlier for my var and stdev value.
#This was because the original array used np.random.random & that gives a biased array of uniform distribution around the interval [0. 1).
#So because this is biased we need to use 1/N instead of 1/(N-1)
#I can edit my code to use 100 instead of 99 (as N-1 should jsut be N) and I would get the same value as Numpy

#Q4
array = array * array #squares original array
arraymean = np.sum(array) / 100 #calculates the mean value of new array
print("A4.1: The mean value of the squared array is: " + str(arraymean)) #prints mean value
var = 1 / 99 * np.sum((array - arraymean) * (array - arraymean)) #calculates variance of squared array
print("A4.2: The variance of the squared array is: " + str(var)) #prints var
stdev = np.sqrt(var) #calculates standard deviation of squared array
print("A4.3: The standard deviation of the squared array is: " + str(stdev)) #prints stdev

