number = input("Enter the number")
counter = 1
if int(number)==0 | int(number==1):
    print("you have inputted o or 1")
else:
    for numm in range(2, (int(number)+1)):
        for num in range(2, (numm+1)):
            if numm % num == 0:
                counter+=1
        if counter>2:
            pass
        else:
            print(numm)
        counter=1
        