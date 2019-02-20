import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

##############################################################################

# Settings for projectile / equation
c = 0.65  # constant of atmospheric friction (kg/s)
g = 9.81  # gravity (m/s**2)
m = 0.1  # mass (kg)
v0 = 10.0  # initial velocity of projectile (m/s)
theta = 50.0  # angle above horizontal (degrees)
t0 = 0.0  # initial time (s)
tmax = 1  # guess of maximum time fortravel [must be greater actual time] (s)
steps = 500  # number of steps time steps desired (no units)
x0 = 0.0  # initial x position (m)
y0 = 0.0  # initial y position (m)
npnts = 20   # number of points desired for end plot (no units)

##############################################################################

# Calculations

thetarad = theta/180.0*np.pi  # concerts theta to radians
vx0 = v0*np.cos(thetarad)  # calculates initial x velocity
vy0 = v0*np.sin(thetarad)  # calculates initial y velocity
vt = m*g/c  # calculates terminal velocity

# makes array of evenly spaced steps with number of time steps = steps
# (+1 for the initial time), and initial time of t0
tAF = np.linspace(t0, tmax, steps+1)

# creates array of float of initial x position, initial y postion,
# initial x velocity, and initial y velocity
y0AF = np.array([x0, y0, vx0, vy0])

# array_of_float array_of_float -> array_of_float
# takes an array of current positions and velocities, and an array of timesteps
# and updates them using odeint()


def dvdtAF(yAF, tAF):
    x = yAF[0]  # this is the x position of the projectile [0th]
    y = yAF[1]  # this is the y position of the projectile [1st]
    vx = yAF[2]  # this is the x velocity of the projectile [2nd]
    vy = yAF[3]  # this is the y velocity of the projectile [3rd]
    return np.array([vx, vy, -c*vx/m, -g-c*vy/m])
# calculation of change in variable of each variable given in array
# postion x and y both increase by vx*t and vy*t respectively
# velocity vx decreases by atmospheric drag -c*vx*t/m
# velocity vy decreases by atmospheric drag and grav acceleration -g*t-c*vy*t/m


# array_of_float -> array_of_float
# takes an array of time steps, and calculates
# analytic solution for each timestep giving array of x and y values
# with x values being 0th colm, and y values being 1st colm

def analyticAF(tAF):
    x = v0*vt/g*np.cos(thetarad)*(1-np.exp(-g/vt*tAF)) + x0
    y = vt/g*(v0*np.sin(thetarad)+vt)*(1-np.exp(-g/vt*tAF))-vt*tAF + y0
    return np.transpose(np.array([x, y]))


ysoln = odeint(dvdtAF, y0AF, tAF)  # solves differential equation
analy = analyticAF(tAF)  # analytical solution x and y values based on t

posbool = ysoln[:, 1] >= 0  # array of true for positive y in equation
approx = ysoln[posbool]  # selects points corresponding to posbool
tapprox = tAF[posbool]  # time coords corresponsing to posbool
analyt = analy[posbool]  # selects points corresponsing to posbool
tmaxnew = tapprox[-1]  # stores calculated tmax value to use in plotting

# new time range to find npnts number of points on graph
tAFnew = np.linspace(t0, tmaxnew, npnts)

# calculates npnts on graph
npntsapprox = odeint(dvdtAF, y0AF, tAFnew)

##############################################################################

# Plots

# plots the approximation values
plt.plot(npntsapprox[:, 0], npntsapprox[:, 1], "r.", label="Approx Position")
# plots the analytic values
plt.plot(analyt[:, 0], analyt[:, 1], "b--", label="Analytic Position")

plt.xlabel("x-position")  # labels x axis
plt.ylabel("y-position")  # labels y axis
# adds title to plot
plt.title("Approximated and Analytic Solution for $m*dv/dt=-m*g-c*v$")
plt.legend()  # adds legend to plot
plt.savefig("ballistic.pdf")  # saves plot

##############################################################################

# Print Statements

# distance to impact is final x position in x position column
print("Distance to impact is D={}m".format(approx[:, 0][-1]))

# maximum height is max value in y position column
print("The maximum height reached is H={}m".format(np.max(approx[:, 1])))

# time of flight is value of final time step or last t value in t array
print("The time if flight is T={}s".format(tmaxnew))

# final velocity's components is last vx and last vy corresponding
# to final positive or zero y value
print("The final velocity v=<{},{}>m/s".format(approx[:, 2][-1],
                                               approx[:, 3][-1]))

