import numpy as np #imports numpy as abbreviated np
import matplotlib.pyplot as plt #imports laplotlib.pyplot as abbreviated plt

#complex_number int -> tuple
#calculates the convergent root for given starting point after iter number of iterations of newton's method and gives number of iterations needed to 
def which_root_z4(start, iter=100):
    i = range(0, iter) #creates range to count for for loop
    for cnt in i: #for loop calculating newtons method iter number of times
        start = start - (start*start*start*start - 1)/(3 * start*start*start)
        complex(start)
        currentiter = cnt #stores current number of iterations done
        if (np.abs(start) < 0.25): #checks if dist from origin < 0.25 and breaks if true
            break
    result = start
    if (np.abs(result.real) > np.abs(result.imag)): #determines if convergent root is real or imaginary
        if (result.real > 0):
            return (0, currentiter)  #means tends towards root 1
        else:
            return (2, currentiter)   #means tends towards root -1
    elif (np.abs(result.real) < np.abs(result.imag)): #guards against equal real and imaginary
        if (result.imag > 0):
            return (1, currentiter)  #means tends towards root i
        else:
            return (3, currentiter)  #means tends towards root -i
    else:
        return (4, currentiter)  #means does not converge within iterations

xrange = np.arange(-2,2,0.04) #creates range of 100 x values from -2 to 2 and stores in xrange
yrange = np.arange(-3,3,0.06) #creates range of 100 y values from -3 to 3 and stores in yrange

imagegrid = np.zeros((100,100,3)) #creates empty 3D array to store color data in

i1 = range(0, 100) #creates two lists of 100 elements to count for for loop
i2 = range(0, 100)

#calculates complex number for each value x and y making a complex number x + jy and then calculates the convergent root and finally enters in a value of 1 at z of the imagegrid corresponding to its position, depending on root index
for cnt1 in i1: 
    currentx = xrange[cnt1] #stores current x value in currentx
    for cnt2 in i2: #calculates complex, calculates convergent root and enters data in 3d grid depending on index number
        n = 20 #desired number of iterations
        currentcomplex = currentx + (yrange[cnt2]*1j) #gives the complex number
        roottuple = which_root_z4(currentcomplex, n) #calculates convergent root and storesinroot tuple
        shading = (n-roottuple[1])/n
        if (roottuple[0] == 0): #if converges to 1 or index 0 colours point red
            imagegrid[cnt2, cnt1, 0] = 255 * shading
        elif (roottuple[0] == 1): #if converges to i or index 1 colours point green
            imagegrid[cnt2, cnt1, 1] = 255 * shading
        elif (roottuple[0] == 2): #if converges to -1 or index 2 colours point blue
            imagegrid[cnt2, cnt1, 2] = 255 * shading
        elif (roottuple[0] == 3): #if converges to -i or index 3 colours point pink
            imagegrid[cnt2, cnt1, 0] = 255 * shading
            imagegrid[cnt2, cnt1, 1] = 0
            imagegrid[cnt2, cnt1, 2] = 255 * shading
        else: #if doesnt converge sets to point to black
            imagegrid[cnt2, cnt1, 0] = 0
            imagegrid[cnt2, cnt1, 1] = 0
            imagegrid[cnt2, cnt1, 2] = 0

plt.imshow(imagegrid, extent=(-2,2,-3,3)) #plots grid of convergent roots with extents from x -2 to 2 and y -3 to 3
plt.xlabel("Real Numbers") #labels x axis as real numbers
plt.ylabel("Imaginary Numbers") #labels y axis as imaginary numbers   
plt.title("Lowres Graph of Convergent Roots") #gives title of graph
plt.savefig("newton_highrestest.pdf") #saves lowres pdf
