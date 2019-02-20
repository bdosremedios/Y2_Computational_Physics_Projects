import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

##############################################################################

# Parameters

L = float(input("Please enter inductance: "))  # sets user's desired L
C = float(input("Please enter capacitance: "))  # sets user's desired C
V0pp = 1.0  # initial voltage peak to peak
m = np.array([0.2, 1, 5])  # underdamp, crit damp, and overdamp m values
t0 = 0.0  # start time
steps = 500  # number of time steps
points = 200  # number of points for frequency

##############################################################################

# Calculations

V0 = V0pp/2  # finds amplitude voltage
w0 = 1/np.sqrt(L*C)  # calculates natural angular frquency
tmax = 20*2*np.pi/w0+t0  # tmax long such that accurate current can be calced
# array of underdamped, crit damped, and overdamped resistance
rAF = np.array([2*m[0]*np.sqrt(L/C),  # calcs underdamped R
                2*m[1]*np.sqrt(L/C),  # calcs critically damped R
                2*m[2]*np.sqrt(L/C)])  # calcs overdamped R
# list of names for each resistance for various uses, corresponding to rAF
namesAS = (["Underdamped", "Critically Damped", "Overdamped"])
fAF = np.linspace(0.05*w0/np.pi, w0/np.pi, points)  # calcs array for freq
tAF = np.linspace(t0, tmax, steps)  # calcs long time array for resonance calc
iAF = np.array([0,  # initial current in circuit
                0,  # initial change in current
                0])  # initial wt term


# function for odeint, diff eq. for LRC circuit
def LCR(iAF, tAF):
    dq = iAF[0]  # current of the circuit
    d2q = iAF[1]  # change in current
    wt = iAF[2]  # current angular frquency
    # update for current dq is d2q
    # update for d2q: derivative of everything in diff eq and solved for d3q
    # update for wt term, is derivate which is just w
    return np.array([d2q,
                     (-V0*np.sin(wt)*w-R*d2q-dq/C)/L,
                     w])


reslist = []  # list to store all frequency data for each R

# calcs current from frequency range for each resistance
for R in rAF:
    freqlist = []  # current storage list for each freq for this resistance
    # calcs the current after the transient portion for each frequency
    for f in fAF:
        w = 2*np.pi*f  # changes the freq to ang freq
        temparr = odeint(LCR, iAF, tAF)[:, 0]  # calcs diff eq for freq
        # chooses the peak current after half the waves, which will be
        # current well after the stabilization, and stores in freqlist
        freqlist.append(max(temparr[temparr.size//2:temparr.size]))
    # stores list of currents in reslist corresonding to each resistance
    reslist.append(np.array(freqlist))

# tmax short so evolution can be seen, in this case being 3 wavelengths
tmax = 3*2*np.pi/w0+t0
tAF = np.linspace(t0, tmax, steps)  # make short time array for time evolution
evolist = []  # List to store time evolution data for each R
w = w0  # Resets w to be natural angular freq

# calcs time evolution for each resistance
for R in rAF:
    # calculates time evolution of resistance and stores in evolist
    evolist.append(odeint(LCR, iAF, tAF)[:, 0])

##############################################################################

# Plots

fig = plt.figure()
# adds title to resonance graph
fig.suptitle("Resonance graphs for each Resistance", fontweight="bold")
# creates graph of current for each freq in freq range for each R
for i1 in range(3):
    plt.subplot(311 + i1)  # makes 3 by 1 subplot of index 1 + i1
    plt.plot(fAF, reslist[i1])  # plots current vs frequency
    # adds title with all variables set to 2 sigfigs and font size 10
    plt.title("{0} R={1:.2g} L={2:.2g} C={3:.2g}".format
              (namesAS[i1], rAF[i1], L, C),
              fontsize=10)
    plt.xlabel("Frequency (Hz)")  # adds x label
    plt.ylabel("Current (A)")  # adds y label
plt.subplots_adjust(hspace=1.2, wspace=0.6)  # adds spacing between subplots
plt.savefig("resonance.pdf")  # saves as resonance.pdf
plt.clf()  # clears the figure to make way for time graphs

fig = plt.figure()
# adds title to time graph
fig.suptitle("Time evolution graphs for each Resistance", fontweight="bold")
# creates graph of current for each freq in freq range for each R
for i2 in range(3):
    plt.subplot(221+i2)  # makes 2 by 2 subplot of index 1 + i2
    plt.plot(tAF, evolist[i2])  # plots current vs time
    # adds title with all variables set to 2 sigfigs and font size 10
    plt.title("{0} R={1:.2g} L={2:.2g} C={3:.2g}".format
              (namesAS[i2], rAF[i2], L, C),
              fontsize=10)
    plt.xlabel("Time (s)")  # adds x label
    plt.ylabel("Current (A)")  # adds y label
plt.subplots_adjust(hspace=0.6, wspace=0.4)  # adds spacing between subplots
plt.savefig("transients.pdf")  # saves as transients.pdf
