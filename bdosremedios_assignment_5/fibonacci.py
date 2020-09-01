# int -> number
# returns the nth number of the fibonacci sequence
def fibonacci(n):
    def recur(z,f1=1,f2=1):
        if z==1:
            return 1
        if z==2:
            return 1
        if z==3:
            return f1+f2
        return recur(z-1,f1=f2,f2=f1+f2)
    answer = recur(n)
    return answer

f=open('fibonacci.txt','w')
f.write("n  " + "Fn" + "\n")
f.write("1  " + str(fibonacci(1)) + "\n")
f.write("2  " + str(fibonacci(2)) + "\n")
f.write("3  " + str(fibonacci(3)) + "\n")
f.write("4  " + str(fibonacci(4)) + "\n")
f.write("5  " + str(fibonacci(5)) + "\n")
f.write("6  " + str(fibonacci(6)) + "\n")
f.write("7  " + str(fibonacci(7)) + "\n")
f.write("8  " + str(fibonacci(8)) + "\n")
f.write("9  " + str(fibonacci(9)) + "\n")
f.write("10 " + str(fibonacci(10)) + "\n")
f.write("11 " + str(fibonacci(11)) + "\n")
f.write("12 " + str(fibonacci(12)) + "\n")
f.write("13 " + str(fibonacci(13)) + "\n")
f.write("14 " + str(fibonacci(14)) + "\n")
f.write("15 " + str(fibonacci(15)) + "\n")
f.write("16 " + str(fibonacci(16)) + "\n")
f.write("17 " + str(fibonacci(17)) + "\n")
f.write("18 " + str(fibonacci(18)) + "\n")
f.write("19 " + str(fibonacci(19)) + "\n")
f.write("20 " + str(fibonacci(20)) + "\n")
f.write("21 " + str(fibonacci(21)) + "\n")
f.close

