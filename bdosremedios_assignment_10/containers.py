# list -> list
# takes a list and returns a list of the first and last elements
def list2ends(t):
    if (t == []): #returns 0th element and last element in list unless list is empty in which case it returns t 
        list = t
    else:
        list = (t[0],t[-1])
    return list

# list -> list
# takes a list and removes all duplicates
def noduplicates(t):
    list = [] #creates empty new list
    for entry in t: #for loop checking each value of t
        if (list.count(entry) == 0): #checks if entry if part of new list yet and adds if it is
            list = list + [entry] # adds entry to list
    return list #returns list

# list -> list
# takes a list of numbers and returns a list containing elements smaller than 10 w.o duplicates
def lessthanten(t):
    list = [] #creates empty new list
    for entry in t: #for loop checking each value in t
        if (entry < 10) and (list.count(entry) == 0): #checks if entry less than 10 and not in list adds to new list if is
            list = list + [entry] #adds entry to newlist
    return list #returns list

# list -> list
# takes list and modifies in place to remove first and last entry
def truncate(t):
    if (t != []): #checks if not emptylist and removes first if isnt
        t.remove(t[0]) #removes first variable in place
        t.reverse() #reverses list
        if (t != []): #checks again if not empty list and removes last if isnt
            t.remove(t[0]) #removes first variable of reversed list
            t.reverse() #reverses list back to right orientation
    return None #returns none

# dictionary dictionary dictionary -> dictionary
# returns concatenate of three dictionaries
def concatenate(a, b, c):
    b.update(c) #concatenates dictionary c to b
    a.update(b) #concatenates dictionary b to a
    return a #returns a

# dictionary key -> string
# returns string saying key exits if key exists in dicitonary and does not exits if key does not exist in dictionary
def exists(d, s):
    listkeys = [*d.keys()] #stores list of d's keys
    if (listkeys.count(s) > 0): #checks if s is in list of keys
        return ("key {} already exists in dictionary".format (s)) #returns string if true
    else:
        return ("key {} does NOT exist in dictionary".format (s)) #returns string if key not in
