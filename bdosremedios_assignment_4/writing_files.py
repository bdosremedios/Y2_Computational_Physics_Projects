import numpy as np #imports numpy as np
data = np.loadtxt('/home2/phys210/Public/examplearray.txt') #loads data from examplearray.txt
datacol2 = np.loadtxt('/home2/phys210/Public/examplearray.txt', usecols=1) #loads data from column 2
datacol3 = np.loadtxt('/home2/phys210/Public/examplearray.txt', usecols=2) #loads data from column 3
mean2 = np.mean(datacol2) #calculates mean of 2 and stores in mean2
var3 = np.var(datacol3) #calculates var of 3 and stores in var3
f=open('stats.txt', 'w') #opens stats.txt to write
f.write("Mean[y] = " + str(mean2) + "\n") #writes mean in file and goes to next line
f.write("Var[y] =" + str(var3)) #writes var in file
f.close #closes stats.txt
datax = 1000 * data[:,1] #takes x column from data and increases by factor 1000
dataalter = data #creates copy of array to insert x into
dataalter[0,1] = datax[0] #replaces 2nd column 1st element in array with factor 1000 does same for all below
dataalter[1,1] = datax[1]
dataalter[2,1] = datax[2]
dataalter[3,1] = datax[3]
dataalter[4,1] = datax[4]
dataalter[5,1] = datax[5]
np.savetxt ("data_new.txt", dataalter) #stores altered array in file data_new.txt
