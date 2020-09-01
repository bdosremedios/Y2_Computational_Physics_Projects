import numpy as np #imports numpy with abbreviation np
#Q1
array = np.array([0,1,2,3,4,5,6,7,8,9]) #creates array from 0 to 9 in array
print("A1: This is the array from 0 to 9: " + str(array)) #prints array
#Q2
array = array * array #squares values in array
print("A2: The squared array is: " + str(array)) #prints array
#Q3
array = np.sqrt(array) 
#takes square root of previous array
print("A3: The square root of last question's array is: " + str(array)) #prints array
#Q4
array = np.array([1,2,3,4,5,6,7,8,9]) #makes array of 1 to 9
array = 4 / 3 * np.pi * array * array * array #calculates shperical volume of each number as of it were a radius of a sphere
print("A4: The volumes of spheres of radii 1 to 9 respectively are: " + str(array)) #prints array
#Q5
array = 2 * np.pi *  np.random.random((1,12)) #creates size 12 random list on [0, 2pi)
print("A5: The size 12 random array from 0 to 2pi is: " + str(array)) #prints array
#Q6
array = np.sin(array) #takes sine of each value in previous array
print("A6: The sin of the previous array is " + str(array)) #prints array
