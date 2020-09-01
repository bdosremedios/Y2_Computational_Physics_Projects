import numpy as np #imports numpy as abbreviated np
data = np.loadtxt('/home2/phys210/Public/examplearray.txt') #loads data from examplearray.txt in data
oldstring = "Data-point number %i has values of x=%f and y=%f, with errors of %f and %f, respectively." #sets up string template
print(oldstring % (data[1,0],data[1,1],data[1,2],data[1,3],data[1,4])) #prints sentence for row 2
print(oldstring % (data[2,0],data[2,1],data[2,2],data[2,3],data[2,4])) #prints sentence for row 3
newstring = "Data-point number {} has values of x={} and y={}, with errors of {} and {}, respectively." #sets up new string
print(newstring.format (data[1,0],data[1,1],data[1,2],data[1,3],data[1,4])) #prints sentence for row 2 using new method
print(newstring.format (data[2,0],data[2,1],data[2,2],data[2,3],data[2,4])) #prints sentence for row 3 using new method
pathstring = "/home2/{}/{}_assignment_{}/{}" #sets up string template for 3
username = "bdosremedios" #stores username
assignnum = 4 #stores assignment number
filename = "string_formatting.py" #stores file name
print(pathstring.format(username,username,assignnum,filename)) #prints path to file
