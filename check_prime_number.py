number = input("Enter the number to check prime number or not")
counter = 1
for num in range(2, (int(number)+1)):
    if int(number) % num == 0:
        counter+=1
if counter > 2:
    print("It is not a prime number")
else:
    print("It is a prime number")