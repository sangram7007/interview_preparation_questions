#write a program to check is it armstrong or not ?

input_number = input("enter your number\n")
print(input_number)
number_length = len(input_number)
print(number_length)
sum=0
for value in input_number:
    val = int(value)**number_length
    sum+=val
    
print(sum)
if int(input_number) == sum:
    print('your number is a armstrong number')
else:
    print('Your number is not armstrong number')