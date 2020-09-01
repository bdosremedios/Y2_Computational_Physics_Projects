import numpy as np #imports numpy

# np.array -> print statement
# array is np.array of which mean is wanted
# calculates and prints mean of array
def calcmean(array):
    mean = np.sum(array) / np.size(array) # mean is calculated mean of array
    print("The mean is {}".format (mean))

# np.array -> print statement
# array is np.array of which var is wanted
# calculates and prints variance of array
def calcvar(array):
    mean = np.sum(array) / np.size(array) # mean is calculated mean of array usign calcmean code
    var = 1 / (np.size(array)-1) * np.sum((array - mean)*(array - mean))
    # var is calculated variance of array
    print("The variance is {}".format (var))

# np.array -> print statement
# array is np.array of which std is wanted
# calculates and prints standard deviation of array
def calcstd(array):
    mean = np.sum(array) / np.size(array) #mean is calculated using mean code
    var = 1 / (np.size(array)-1) * np.sum((array - mean)*(array - mean)) # var is calculated var of array using calcvar code
    std = np.sqrt(var) # std is calculated standard deviation of array
    print("The standard deviation is {}".format (std))
