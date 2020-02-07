#to take input from user
#num=int(input("enter a numbers:"))
num=int(input('enter any number:'))
#to check the number is positive or negative.
factorial=1
if num<0:
    print("the factorial of negative numbers is not exist")
elif num==0:
    print("the factorial is 0 is 1")
for i in range (1,num+1):
 factorial=factorial*i
print('the factorial of num is',factorial)



