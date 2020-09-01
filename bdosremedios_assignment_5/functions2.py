import numpy as np #imports numpy

# string int -> np.array
# uses filename entered as stringand a number and loads the file of filename 
# returning the i column
def loadcolm(filename, i):
    colm=np.loadtxt(filename, usecols=i)
    return colm

a = loadcolm("examplearray.txt", 3) #loads 3rd column as a

import stats as s #imports stats.py i made

s.calcmean(a) #calculates and prints mean of a
s.calcvar(a) #calculates and prints var of a
s.calcstd(a) #calculates and prints std of a
