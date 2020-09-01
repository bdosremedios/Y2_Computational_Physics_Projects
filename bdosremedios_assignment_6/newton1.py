import numpy as np #imports numpy as abbreviation np

#complex_number int -> int or string
#calculates the convergent root for given starting point after iter number of iterations of newton's method
def which_root_z4_recursive(start, iter):
    def loop_iter(start, iter): #recursive function to calculate convergent root
        if (iter == 0): #ends is iterations have all run through
            return start
        else:
            x = start - (start*start*start*start - 1)/(3 * start*start*start)
            complex(x)
            return loop_iter(x, iter - 1)
    result = loop_iter(start,iter)
    if (np.abs(result.real) > np.abs(result.imag)): #determines if convergent root is real or imaginary
        if (result.real > 0):
            return 0 #means tends towards root 1
        else:
            return 2 #means tends towards root -1
    elif (np.abs(result.real) < np.abs(result.imag)): #guards against equal real and imaginary
        if (result.imag > 0):
            return 1 #means tends towards root i
        else:
            return 3 #means tends towards root -i
    else:
        return "Can't calculate root" #gives result if root cant be calculated

#complex_number int -> int or string
#calculates the convergent root for given starting point after iter number of iterations of newton's method
def which_root_z4(start, iter):
    while (iter!=0): #while loop calculating newtons method iter number of times
        start = start - (start*start*start*start - 1)/(3 * start*start*start)
        complex(start)
        iter = iter - 1
    result = start
    if (np.abs(result.real) > np.abs(result.imag)): #determines if convergent root is real or imaginary
        if (result.real > 0):
            return 0 #means tends towards root 1
        else:
            return 2 #means tends towards root -1
    elif (np.abs(result.real) < np.abs(result.imag)): #guards against equal real and imaginary
        if (result.imag > 0):
            return 1 #means tends towards root i
        else:
            return 3 #means tends towards root -i
    else:
        return "Can't calculate root" #gives result if root cant be calculated
    
z1=1.2+0.2j
print("Using the recursive function, {} converges to index {}".format (z1, which_root_z4_recursive(z1,50)))
print("Using the while loop function, {} converges to index {}".format (z1, which_root_z4(z1,50)))
z2=0.2+0.9j
print("Using the recursive function, {} converges to index {}".format (z2, which_root_z4_recursive(z2,50)))
print("Using the while loop function, {} converges to index {}".format (z2, which_root_z4(z2,50)))
z3=-0.8+0.1j
print("Using the recursive function, {} converges to index {}".format (z3, which_root_z4_recursive(z3,50)))
print("Using the while loop function, {} converges to index {}".format (z3, which_root_z4(z3,50)))