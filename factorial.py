num=8
#to take input from user
#num=int(input("enter a numbers:"))
factorial=1
#to check the number is positive or negative.
if num<0:
    print("the factorial of negative numbers is not exist")
elif num==0:
    print("the factorial is 0 is 1")
    for i in range (1,num):
        factorial=factorial*i
        print(factorial)



