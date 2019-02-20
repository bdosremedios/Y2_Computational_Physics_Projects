import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

##############################################################################

# Parameters

# array of temperatures (K)
temp = np.array([0.01, 0.1, 1, 2, 2.5, 3, 4, 5, 10, 100])
animate = [0.1, 2.5, 100]  # temperatures desired to be animated
Jij = 1.0  # Jij
iter = 600000  # num. of iterations for each M
itertemp = 5  # num. of interations for each temperature
mu = 1.0  # Magnetic constant

##############################################################################

# Calculations and Animation Generation

# create array of 1 and -1, 2500 size randomly
rand = np.random.choice(np.array([-1, 1]), size=2500)
# turns rand to 50x50
rand = np.reshape(rand, (50, 50))

# creates array to store each max M value for each temp
storM = np.zeros(temp.size)

# performs loop on each temperature
for cnt1 in range(temp.size):
    # sets t as temperatire currently being calculated
    t = temp[cnt1]
    # finds if t needs to be animated
    shdanimate = t in animate
    # creates an empty array to store iterated Ms
    tempMarr = np.zeros(itertemp)
    # reruns code itertemp times and finds a max value of M
    for cnt2 in range(itertemp):
        # checks if on first iteration cycle and needs animation
        shdanimate = shdanimate and (cnt2 == 0)
        # creates copy of rand array to alter in each
        randt = rand.copy()
        # runs normal loop if dont need to animate and other if does
        if not shdanimate:
            # iterates the random config change and choice iter times
            for i in np.arange(iter):
                # generates two random numbers within [0, 49]
                row = np.random.choice(50)
                colm = np.random.choice(50)
                # finds values above, below, left, right and opposite of point
                flip = -randt[row, colm]
                up = randt[row-1, colm]
                try:  # checks if goes past index bounds and corrects for it
                    down = randt[row+1, colm]
                except:  # gives unerrored other side value if at end
                    down = randt[-1, colm]
                left = randt[row, colm-1]
                try:  # checks if goes past index bounds and corrects for it
                    right = randt[row, colm+1]
                except:  # gives unerrored other side value if at end
                    right = randt[row, -1]
                # calculates difference by finding new energy on sigmaprime
                Hdiff = -Jij*flip*(up+down+left+right)
                # using energy diff from new config, use config if lower
                # (negative), and if higher (postive), calculate probability
                # and if under probability use config
                if (Hdiff <= 0):
                    randt[row, colm] = flip
                else:
                    if (np.random.random(1)[0] <= np.exp((Hdiff)/-t)):
                        randt[row, colm] = flip
            # stores iteration of avg mag moment value in empty array
            tempMarr[cnt2] = mu*sum(sum(randt))
        else:
            # creates list to record images w/ figure for animate
            ims = []
            fig = plt.figure()
            # same code as above but records an animation frame every 6000 i
            for i in range(iter):
                # adds a frame every 1000 steps
                if (i % 1000 == 0):
                    ims.append((plt.pcolor(randt),))
                row = np.random.choice(50)
                colm = np.random.choice(50)
                flip = -randt[row, colm]
                up = randt[row-1, colm]
                try:
                    down = randt[row+1, colm]
                except:
                    down = randt[-1, colm]
                left = randt[row, colm-1]
                try:
                    right = randt[row, colm+1]
                except:
                    right = randt[row, -1]
                Hdiff = -Jij*flip*(up+down+left+right)
                if (Hdiff <= 0):
                    randt[row, colm] = flip
                else:
                    if (np.random.random(1)[0] <= np.exp((Hdiff)/-t)):
                        randt[row, colm] = flip
            tempMarr[cnt2] = mu*sum(sum(randt))
            # labels plot, creates and saves animation, then clears plot
            plt.title("Equilibrium Progression of T={}K".format(t))
            imgani = animation.ArtistAnimation(fig, ims, interval=50,
                                               blit=False, repeat=False)
            imgani.save("temp_{}.mp4".format(t))
            plt.clf()
    # stores maximum absolute value of M for each temperature
    storM[cnt1] = np.max(np.abs(tempMarr))

##############################################################################

# Plots

# plots max M value as function of log of temperature
plt.plot(np.log(temp), storM, "r")
plt.xlabel("Log of Temperature")  # labels x axis
plt.ylabel("Max Avg. Magnetic Moment")  # labels y axis
plt.title("Magnetic moment vs. log(Temperature)")  # adds title to plot
plt.savefig("Tcurie.pdf")  # saves plot as a PDF

##############################################################################
