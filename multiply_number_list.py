# Python program to multiply all values in the list using traversal


def multiplylist(mylist):
    # Multiply elements one by one
    result = 1
    for x in mylist:
        result = result * x
    return result


list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiplylist(list1))
print(multiplylist(list2))
