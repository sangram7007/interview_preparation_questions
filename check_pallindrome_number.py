number = input("enter the number")
n=0
def reverse(number):
   n = number[::-1]
   return n
result = reverse(number)
if number==result:
    print("it is pallindrome number")
else:
    print("it is not a pallindrome number")