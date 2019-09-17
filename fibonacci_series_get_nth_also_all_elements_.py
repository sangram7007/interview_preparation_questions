n = int(input("enter the number"))
fib_array = []
a = 0
b = 1
fib_array.append(a) #first element should be 0
fib_array.append(b) #second element should be 1
if n < 0: 
    print("Incorrect input") 
elif n == 0: 
    print(a) 
elif n == 1: 
    print(b) 
else: 
    for i in range(2,n+1): #after 0 and 1 series addition will happen to get the result
        c = a + b 
        fib_array.append(c)
        a = b 
        b = c 
    print(b) 
    print(fib_array)
    for val in fib_array:
        print(val)