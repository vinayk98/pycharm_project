# Python3 program to swap first  and last element of a list Swap function
def swaplist(newlist):
    newlist[0], newlist[-1] = newlist[-1], newlist[0]

    return newList


# Driver code
newList = [12, 35, 9, 56, 24]
print(swaplist(newList))
