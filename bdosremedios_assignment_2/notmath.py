#Question 1
import math
radius = 3 #sets radius to 3
volume = 4/3*math.pi*radius*radius*radius #calculates sphere volume of radius radius and sets value to variable volume
print("Q1: The volume is " + str(volume)) #converts volume to string and prints wit header

#Question 2
area = 15 #sets area to 15
length = math.sqrt(area) #takes the square root of the area of calculate side length and sets length to that value
print("Q2: The side length is " + str(length)) #converts length to string and prints with header

#Question 3
degreevalue = 121 #sets degreevalue to 121
radianvalue = degreevalue/180*math.pi #calculates 121 in radians and sets to radianvalue
sin=math.sin(radianvalue) #calculates sin of raidanvalue
cos=math.cos(radianvalue) #calculates cos of raidanvalue
tan=math.cos(radianvalue) #calculates tan of raidanvalue
print("Q3 The sin, cos, and tan of 121 degrees respectively are " + str(sin) + ", " + str(cos) + ", and " + str(tan)) # convers sin cos and tan to strings and rint them with header
