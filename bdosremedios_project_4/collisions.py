import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from itertools import combinations as comb
from scipy.optimize import curve_fit as curv

##############################################################################

# Parameters

npnt = 400  # number of particles (no units)
steps = 1000  # number of time steps (no units)
dt = 0.00002  # length of time step (s)
size = 0.0015  # radius of particle (m)
mass = 2.672e-26  # mass of particle (kg)
xmin, xmax, ymin, ymax = 0, 1, 0, 1  # limits of positions (m)
kb = 1.38e-23  # Boltzmann constant (s^-2*K^-1)
nbin = 10  # Number of bins for histograms (no units)
sizesqr = (2*size)**2  # calcs 2 times size squared (m^2)

##############################################################################

# Plots

fig, ax = plt.subplots()
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)


# function to update particles of the plot, the particles hitting the wall
# having velocites be reversed and colliding particles having velocities
# changed depending on momuntum conservation equations
def update_point(num):
    global x, y, vx, vy
    print(num)
    indx = np.where((x < xmin) | (x > xmax))
    indy = np.where((y < ymin) | (y > ymax))
    vx[indx] = -vx[indx]
    vy[indy] = -vy[indy]
    xx = np.asarray(list(comb(x, 2)))
    yy = np.asarray(list(comb(y, 2)))
    dd = (xx[:, 0]-xx[:, 1])**2+(yy[:, 0]-yy[:, 1])**2

    indx = np.array(range(x.size))  # creates index corresponsing to x/y
    indxx = np.array(list(comb(indx, 2)))  # index corresponding to xx/yy
    colpnt = (dd <= sizesqr)  # bool for points within one anothers radii
    indcol = indxx[colpnt]  # array of pairs of indices for colliding points
    ind0 = indcol[:, 0]  # array of indices of first colliding points
    ind1 = indcol[:, 1]  # array of indices of second colliding points
    # finds arrays of first colliding points' x, y, vx, and vy
    x1arr, y1arr, vx1arr, vy1arr = x[ind0], y[ind0], vx[ind0], vy[ind0]
    # finds arrays of second colliding points' x, y, vx, and vy
    x2arr, y2arr, vx2arr, vy2arr = x[ind1], y[ind1], vx[ind1], vy[ind1]
    x1minusx2 = x1arr-x2arr  # calculates the difference between x2 and x1
    y1minusy2 = y1arr-y2arr  # calculates the difference between y2 and y1
    # calcs <v1-v2,x1-x2>/|x1-x2|^2 which is equal to <v2-v1,x2-x1>/|x1-x2|^2
    scalar = ((vx1arr-vx2arr)*(x1minusx2) +
              (vy1arr-vy2arr)*(y1minusy2))/((x1minusx2)**2+(y1minusy2)**2)
    vx[ind0] = vx1arr-scalar*x1minusx2  # calcs/change vx for first particle
    vx[ind1] = vx2arr-scalar*-x1minusx2  # calcs/change vx for second particle
    vy[ind0] = vy1arr-scalar*y1minusy2  # calcs/change vy for second particle
    vy[ind1] = vy2arr-scalar*-y1minusy2  # calcs/change vy for second particle

    dx = dt*vx
    dy = dt*vy
    x = x + dx
    y = y + dy
    data = np.stack((x, y), axis=-1)

    im.set_offsets(data)


x = np.random.random(npnt)
y = np.random.random(npnt)
vx = -500.*np.ones(npnt)
vy = np.zeros(npnt)
vx[np.where(x <= 0.5)] = -vx[np.where(x <= 0.5)]

# empty map of 3 lists of 400 zeroes transposed making 3 x 400 for colors
clr = np.transpose([np.zeros(npnt), np.zeros(npnt), np.zeros(npnt)])
clr[np.where(x <= 0.5)] = (0, 0, 1)  # sets all left x vals to blue
clr[np.where(x > 0.5)] = (1, 0, 0)  # sets all right x vals to red
im = ax.scatter(x, y, c=clr)  # clr is color map of left blue and right red
im.set_sizes([10])
animation = anim.FuncAnimation(fig,
                               update_point, steps, interval=10, repeat=False)
animation.save("collisions.mp4")  # saves animation as mp4 file
plt.close()

fv = np.sqrt(vx**2 + vy**2)  # calcs magnitude of velocity for particles
gE = 1/2*mass*fv**2  # calcs kinetic energy distribution for particles


# function of analytical fv to use for fitting giving unnormalised probability
def fvfunc(v, T):
    return mass*v*np.exp(-(mass*v**2)/(2*kb*T))/(kb*T)


# function for analytical gE giving unnormalised probability
def gEfunc(E, T):
    return np.exp(-E/(kb*T))/(kb*T)


ydata, xdata = np.histogram(fv, bins='auto')  # same array as fv histogram
xdata = (xdata + np.roll(xdata, 1))/2  # avgs adjac. bins
xdata = xdata[1:xdata.size]  # gives mid values of bins corresponding to ydata

# fits data to analytic eq f(v) finding fit parameter for temperature
fitpara, useless = curv(fvfunc, xdata, ydata, p0=100)
fitfvx = np.linspace(0, xdata[-1], 1000)  # many point x array for fit
fvanlyt = fvfunc(fitfvx, *fitpara)  # analytical soln of fV probability
# normalises probability and multiplies by npnt to give number of points
fvfitydata = fvanlyt/np.sqrt(sum(fvanlyt**2))*npnt

ydata, xdata = np.histogram(gE, bins='auto')  # same array as gE histogram
xdata = (xdata + np.roll(xdata, 1))/2  # avgs adjac. bins
xdata = xdata[1:xdata.size]  # gives mid values of bins corresponding to ydata
fitgEx = np.linspace(0, xdata[-1], 1000)  # many point x array for fit
gEanlyt = gEfunc(fitgEx, *fitpara)  # analyt soln of gE prob using git temp
# normalises probability and multiplies by npnt to give number of points
gEfitydata = gEanlyt/np.sqrt(sum(gEanlyt**2))*npnt

plt.subplot(211)  # edits 1st of 2 subplots
plt.hist(fv, bins=nbin)  # plots histogram of speeds w/ nbin bins
plt.plot(fitfvx, fvfitydata, label="f(v) bestfit")
plt.title("Distributions of Speed in Particles")  # adds title to plot
plt.xlabel("Speed (m/s)", fontsize=10)  # labels x axis
plt.ylabel("Number of particles (no units)", fontsize=8)  # labels y axis
plt.legend()  # adds legend to plot

plt.subplot(212)  # edits 2nd of 2 subplots
plt.hist(gE, bins=nbin)  # plots histogram of kinetic energies w/ nbin bins
plt.plot(fitgEx, gEfitydata, label="g(E) bestfit")
plt.title("Distributions of Kinetic Energy in Particles")  # adds plot title
plt.xlabel("Kinetic Energy (J)", fontsize=10)  # labels x axis
plt.ylabel("Number of particles (no units)", fontsize=8)  # labels y axis
plt.legend()  # adds legend to plot

plt.subplots_adjust(hspace=0.7)  # adds horizontal spacing to subplots
plt.savefig("distributions.pdf")  # saves histogram plots as pdf

f = open("collisions.txt", "w")  # opens text file to write
f.write("The fitted temperature is : {} K".format(*fitpara))  # writes temp
f.close()  # closes file
