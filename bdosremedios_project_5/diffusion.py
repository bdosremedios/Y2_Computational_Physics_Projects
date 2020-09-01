import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from scipy.optimize import curve_fit as curv

##############################################################################

# Parameters

L = 1  # side length of square (m)
D = 1e-3  # diffusion constant (no units)
grid = 100  # number of gridpoints per line (no units)
dt = 1e-2  # length of timestep (s)
tmax = 1000  # maximum time (s)
inicon = 10  # initial concentration
plottimes = np.array([0.001, 0.01, 0.1, 1, 10, 100, 1000])  # times to plot
writetimes = np.array([0.1, 1, 10, 100])  # times to write total concentration

##############################################################################

# Calculations/Plots

dx = L/grid  # calculates dx based on side length and num points
tsteps = int(tmax/dt)+1  # number of time steps passing to tmax with steps dt
k = D*dt/dx/dx  # calcs k, because  dx = dy k will be the same for both

C = np.zeros((grid, grid))  # empty grid gridxgrid size to store configuration
C[grid//2, grid//2] = inicon  # places concentration near center
Cnext = np.zeros((grid, grid))  # empty grid of next concentrations

plottimes /= dt  # divides plottimes so they are in number of dts passing
# creates list of times between 0s and 10s to check to add to gaussian curve
gauscheck = np.linspace(0, 10/dt, 30).round()
gaust = []  # list to store time data for gaussian
gausx = np.arange(0, L, dx)  # array of x values of grid for fitting
gauscurv = []  # list to store C data for gaussian

inisum = sum(sum(C))  # calculates initial concentration
writetimes /= dt  # puts writetimes' times in terms of num. dts
f = open("totals.txt", "w")  # open text file to record total conc at writtimes
f.write("Time   Concentration\n")  # adds table titles
f.write("0        {:.3g}\n".format(inisum))  # records initial concentration

clr = plt.figure(1)  # creates figure for subplots of C at plottimes

# applies figure update tsteps times
for cnt in range(tsteps):
    # calculates the concentration change in the x and y direction of array
    changex = k*(np.roll(C, 1, axis=1) + np.roll(C, -1, axis=1) - 2*C)
    changey = k*(np.roll(C, 1, axis=0) + np.roll(C, -1, axis=0) - 2*C)
    # adds concentration changes of middle of array correctly
    Cnext = C + changex + changey
    # adds change in conc. one by one to boundaries to fix roll bound error
    Cnext[:, 0] = C[:, 0] + changex[:, 0]
    Cnext[:, -1] = C[:, -1] + changex[:, -1]
    Cnext[0] = C[0] + changey[0]
    Cnext[-1] = C[-1] + changey[-1]
    # adds conc. changes to corner, as boundary fix only adds one directions'
    for cnt2 in [0, -1]:
        for cnt3 in [0, -1]:
            Cnext[cnt2, cnt3] = changex[cnt2, cnt3] + changey[cnt2, cnt3]
    C, Cnext = Cnext, C  # swaps C/Cnext so next iteration of C can be calced
    # plots time in a subplot, if time is initial time or in plottiimes
    if cnt in plottimes or cnt == 0:
        if cnt == 0:
            cnt = plottimes[0]
        clr.add_subplot(331 + np.where(plottimes == cnt)[0][0])
        plt.pcolormesh(C, label="t = {}".format(cnt*dt))
        plt.title("Concentration at t = {}".format(cnt*dt), fontsize=8)
        plt.xlabel("X-Postion (cm)", fontsize=8)
        plt.ylabel("Y-Postion (cm)", fontsize=8)
        plt.xticks(fontsize=8)
        plt.yticks(fontsize=8)
    # for 30 times between 0 & 10s, records conc. of center row
    if cnt in gauscheck:
        gaust.append(cnt*dt)  # stores the time of the curve
        gauscurv.append(C[grid//2])  # stores the 1-D concentration curve
    # records time and total concentration if time in writetimes
    if cnt in writetimes:
        f.write("{:.3g}        {:.3g}\n".format(cnt*dt, sum(sum(C))))

f.close()  # closes text file
finsum = sum(sum(C))  # calculates final concentration
print("Initial and final concentration:", inisum, finsum)  # print ini/fin conc

plt.tight_layout(h_pad=0, w_pad=0)  # adds proper spacing to subplots
plt.show()  # shows concentration plots at t in plottimes
plt.close(clr)  # closes clr figure to prevent clash


# gaussian function to fit curve data to and find std
def gaussian(x, sigma, A, mu):
    return A*np.exp(-(x-mu)**2/(2*sigma**2))


sigmas = []  # empty list to store sigma(std) data

# adds standard dev for fit at each time in gaus(t)
for data in gauscurv:
    sigmas.append(np.abs(curv(gaussian, gausx, data)[0][0]))

gaus = plt.figure(2)  # creates second figure as gaus

# plots standard deviation of concentration from fit @ sqrt(time) in gaust
plt.plot(np.sqrt(gaust), np.array(sigmas), "ro", label="Data Std")
plt.plot(np.sqrt(gaust),  # plots theoretical eq of std vs sqrt(time)
         np.sqrt(2*D*np.array(gaust)), label="Theoretical")
plt.xlabel("Sqrt Time (sqrt(s))")
plt.ylabel("Standard Deviation")
plt.title("Standard Deviation of Data From Gaussian Fit vs. Time")
plt.legend()
plt.savefig("diffusion.pdf")  # saves gaus as a pdf file
plt.show()
plt.close(gaus)  # closes gaus figure to prevent plot clash

##############################################################################

# Animation

# resets C to initial conditions
C = np.zeros((grid, grid))
C[grid//2, grid//2] = inicon

animcheck = 100/dt  # 100s in dt steps used to limit animation time
ims = []  # storage list for images
clranim, ax = plt.subplots()  # creates figures for animation
plt.title("Diffusion of Initial Concentration = {}".format(inicon))
plt.xlabel("X-Position (cm)")
plt.ylabel("Y-Position (cm)")

# redo earlier code for animation bc animating earlier would cause plot clash
for cnt in range(tsteps):
    changex = k*(np.roll(C, 1, axis=1) + np.roll(C, -1, axis=1) - 2*C)
    changey = k*(np.roll(C, 1, axis=0) + np.roll(C, -1, axis=0) - 2*C)
    Cnext = C + changex + changey
    Cnext[:, 0] = C[:, 0] + changex[:, 0]
    Cnext[:, -1] = C[:, -1] + changex[:, -1]
    Cnext[0] = C[0] + changey[0]
    Cnext[-1] = C[-1] + changey[-1]
    for cnt2 in [0, -1]:
        for cnt3 in [0, -1]:
            Cnext[cnt2, cnt3] = changex[cnt2, cnt3] + changey[cnt2, cnt3]
    C, Cnext = Cnext, C
# adds frame every 0.1s until after 100s
    if cnt <= animcheck and (cnt % 10) == 0:
        print(cnt*dt)
        text = ax.text(0.1, 0.9, "t={:.3g}".format(cnt*dt),
                       bbox=dict(facecolor='white', alpha=0.5),
                       horizontalalignment="center",
                       verticalalignment="center",
                       transform=ax.transAxes)
        ims.append([text, plt.pcolormesh(C), ])

# creates animation of 100s using list of images ims
clranimdone = anim.ArtistAnimation(clranim,
                                   ims, interval=10, blit=True, repeat=False)
clranimdone.save("converges.mp4")  # saves animation as mp4
plt.close(clranim)  # closes clranim figure to open memory
