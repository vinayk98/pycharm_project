# Python program to print Even Numbers in given range

start, end = 4, 19
for num in range(start, end + 1):

    if num % 2 == 1:
        print(num, end=" ")
