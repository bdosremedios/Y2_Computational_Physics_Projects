hello = "Hello" #sets hello to "Hello"
print(hello) #prints hello
world = "World" #sets world to "World"
print(world) #prints world
phys210 = "PHYS210" #sets phys210 to "PHYS210"
print(phys210) #prints phys210
concatenate = hello + world + phys210 #concatenates hello world and phys210 and stores them in concatenate
print(concatenate) #prints concatenate
ubc = "UBC" #sets ubc to "UBC"
UBCconcatenate = concatenate + ubc + ubc + ubc #adds ubc thrice to the end of concatenate and stores in UBC concatenate
print(UBCconcatenate) #prints UBCconcatenate
ubcconcatenate = UBCconcatenate.lower() #makes all letters in UBCconcatenate lowercase and stores in new calue
print(ubcconcatenate) #prints UBCconcatenate with all lowercase letters
ubc1 = ubcconcatenate.replace("o","") #strips occurences of o in string
ubc2 = ubc1.replace("l","") #strips occurences of l in string
print(ubc2) #prints stripped UBC concatenate

