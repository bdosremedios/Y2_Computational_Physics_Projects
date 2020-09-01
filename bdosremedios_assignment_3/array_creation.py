import numpy as np
#Q1
firstarray = np.array([1,2,3,4,5]) #creates array of 1 to 5 and stores in firstarray
print(firstarray) #prints first array
#Q2
secondarray = np.array([1.0,2.0,3.0], dtype=np.float32) #creats array 1 to 3 and changes type to float32 storing in secondarray
print(secondarray) #prints second array
print("This array has type " + str(secondarray.dtype) + " with each number having item size " + str(secondarray.itemsize)) #prints data type and each item size of second array
#Q3
thirdarray = np.arange(501) #creates array of 0 to 500 and stores in thirdarray
#Q4
print(thirdarray[3]) #prints fourth element
print(thirdarray[25]) #prints twenty fifth element
print(thirdarray[100]) #prints hundredth element
print(thirdarray[110]) #prints hundred and tenth element
#Q5
fourtharray = np.random.random((1, 10)) #creates array of 10 numbers on [0, 1)
fourtharray = fourtharray * 2 #multiplies by 2 making range [0,2)
fourtharray = fourtharray - 1 #subtracts 1 making range [-1,1)
print(fourtharray) #prints fourtharray
