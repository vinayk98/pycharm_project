# Python program to print Even Numbers in given range

start, end = 4, 19

# iterating each number in list
for num in range(start, end + 1):

    if num % 2 == 0:
        print(num, end=" ")
