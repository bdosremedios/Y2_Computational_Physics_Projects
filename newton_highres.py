import numpy as np #imports numpy as abbreviated np
import matplotlib.pyplot as plt #imports laplotlib.pyplot as abbreviated plt

#array_of_complex_numbers int -> array_of_int
#calculates the convergent root for each given starting point in array z after iter number of iterations of newton's method and gives root index for each
def which_root_z4_arr(z, iter=100):
    i = range(0, iter) #creates range to count for for loop
    for cnt in i: #for loop calculating newtons method iter number of times
        z = z - (np.power(z, 4)-1)/(3 * np.power(z, 3))
    nonconv = (np.abs(z) > 1) #makes true list of all which did not converge in iterations
    zeros = (np.abs(z) == 0) #makes true list of all which went to 0
    morereal = (np.abs(z.real)) > (np.abs(z.imag)) #makes all with greater real than imag to be true
    moreposr = np.logical_and(morereal, (z.real > 0)) #makes "more real" numbers in array true if positive
    morenegr = np.logical_and(morereal, (z.real < 0)) #makes "more real" numbers in array true if negative
    moreimag = (np.abs(z.real)) < (np.abs(z.imag)) #makes all with greater imag than real to be true
    moreposi = np.logical_and(moreimag, (z.imag > 0)) #makes "more imag numbers in array true if positive i
    morenegi = np.logical_and(moreimag, (z.imag < 0)) #makes "more imag numbers in array true if negative i
    z[moreposr] = 0 # makes all "more real" positive numbers index 0 as they converge to root 1
    z[morenegr] = 2 # makes all "more real" negative numbers index 2 as they converge to root -1
    z[moreposi] = 1 # makes all "more imag" positive numbers index 1 as they converge to root i
    z[morenegi] = 3 # makes all "more imag" negative numbers index 3 as they converge to root -i
    z[nonconv] = 4 #makes all non converging 4 as they did not onverge
    z[zeros] = 4 #makes all zeros 4 as they also would not converge
    return z.real

xrange = np.arange(-2,2,0.004) #creates range of 1000 x values from -2 to 2 and stores in xrange
yrange = np.arange(-3,3,0.006) #creates range of 1000 y values from -3 to 3 and stores in yrange
yrange = yrange * 1j #makes yrange grid of imaginary numbers from -3j to 3j
xmesh,ymesh = np.meshgrid(xrange, yrange) #makes 1000 by 1000 grid of xrange and yrange
complexgrid = xmesh + ymesh #makes grid of complex numbers using ymesh and xmesh
indexarr = which_root_z4_arr(complexgrid) #stores array of root indexes in indexarray
bool0 = indexarr == 0 #creates arrays to give true array to each of the root index values in an 1000 by 1000 array
bool1 = indexarr == 1
bool2 = indexarr == 2
bool3 = indexarr == 3
bool4 = indexarr == 4

imagegrid = np.zeros((1000,1000,3)) #creates empty 3D array to store color data in

imagegrid[bool0] = np.array([255,0,0]) #uses boolean index array to add red colour to all coordinates with root index number 0
imagegrid[bool1] = np.array([0,255,0]) #uses boolean index array to add green colour to all coordinates with root index number 1
imagegrid[bool2] = np.array([0,0,255]) #uses boolean index array to add blue colour to all coordinates with root index number 2
imagegrid[bool3] = np.array([255,0,255]) #uses boolean index array to add pink colour to all coordinates with root index number 3
imagegrid[bool4] = np.array([0,0,0]) #uses boolean index array to add black colour to all coordinates with root index number 4

plt.imshow(imagegrid, extent=(-2,2,-3,3)) #plots grid of convergent roots with extents from x -2 to 2 and y -3 to 3
plt.xlabel("Real Numbers") #labels x axis as real numbers
plt.ylabel("Imaginary Numbers") #labels y axis as imaginary numbers   
plt.title("Highres Graph of Convergent Roots") #gives title of graph
plt.savefig("newton_highres_1.pdf") #saves highres pdf

xrange = np.arange(-1,1,0.002) #creates range of 1000 x values from -1 to 1 and stores in xrange
yrange = np.arange(-1,1,0.002) #creates range of 1000 y values from -1 to 1 and stores in yrange
yrange = yrange * 1j #makes yrange grid of imaginary numbers from -1j to 1j
xmesh,ymesh = np.meshgrid(xrange, yrange) #makes 1000 by 1000 grid of xrange and yrange
complexgrid = xmesh + ymesh #makes grid of complex numbers using ymesh and xmesh
indexarr = which_root_z4_arr(complexgrid) #stores array of root indexes in indexarray
bool0 = indexarr == 0 #creates arrays to give true array to each of the root index values in an 1000 by 1000 array
bool1 = indexarr == 1
bool2 = indexarr == 2
bool3 = indexarr == 3
bool4 = indexarr == 4

imagegrid = np.zeros((1000,1000,3)) #creates empty 3D array to store color data in

imagegrid[bool0] = np.array([255,0,0]) #uses boolean index array to add red colour to all coordinates with root index number 0
imagegrid[bool1] = np.array([0,255,0]) #uses boolean index array to add green colour to all coordinates with root index number 1
imagegrid[bool2] = np.array([0,0,255]) #uses boolean index array to add blue colour to all coordinates with root index number 2
imagegrid[bool3] = np.array([255,0,255]) #uses boolean index array to add pink colour to all coordinates with root index number 3
imagegrid[bool4] = np.array([0,0,0]) #uses boolean index array to add black colour to all coordinates with root index number 4

plt.imshow(imagegrid, extent=(-1,1,-1,1)) #plots grid of convergent roots with extents from x -2 to 2 and y -3 to 3
plt.xlabel("Real Numbers") #labels x axis as real numbers
plt.ylabel("Imaginary Numbers") #labels y axis as imaginary numbers   
plt.title("Zoomed in Interesting Point on Highres Convergent Roots") #gives title of graph
plt.savefig("newton_highres_2.pdf") #saves highres pdf
