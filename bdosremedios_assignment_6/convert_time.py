import time #imports time module

timesince = time.time() #records time from Jan 1, 1970 until now in seconds
dayssince = int(timesince / 86400) #calculates days since epoch
timetoday = timesince - (dayssince * 86400) #calculates time in seconds since
                                         #midnight today
hourstoday = int(timetoday / 3600) #calculates hours since midnight
minutestoday = int((timetoday - hourstoday * 3600)/60) #calculates minutes
                                                       #since midnight after
                                                       #subtracting hours
secondstoday = int(timetoday - hourstoday * 3600 - minutestoday * 60)
#calculates seconds since midnight after subtracting hours and minutes
PSThours = hourstoday - 7 #converts hours UTC to PST
if (PSThours < 0): #corrects PST to normal time if negative
    PSThours = PSThours + 24
print("The UTC time is {}:{}:{}".format (hourstoday,minutestoday,secondstoday))
#prints the UTC time
print("It has been {} days since the epoch".format (dayssince))
#prints days since epoch (for UTC time)
print("The local PST time is {}:{}:{}".format (PSThours,minutestoday,secondstoday))
#prints local PST time
