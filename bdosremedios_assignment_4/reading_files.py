import numpy as np #imports numpy as abbreviated np
data = np.loadtxt('/home2/phys210/Public/examplearray.txt') #loads data from examplearray.txt and stores in data
mean2 = np.mean(np.loadtxt('/home2/phys210/Public/examplearray.txt', usecols = 1)) #loads second column and calculates mean storing in mean2
var3 = np.var(np.loadtxt('/home2/phys210/Public/examplearray.txt', usecols = 2)) #loads col 3 and calculates the variance
print(data) #prints data
print("The {} of the {} column is {}".format("mean","second",mean2)) #prints mean2
print("The {} of the {} column is {}".format("variance","third",var3)) #prints var3
