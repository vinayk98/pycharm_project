# Python3 program to print even length words in a string


def printWords(s):
    # split the string
    s = s.split(' ')

    for word in s:

        # if length is even
        if len(word) % 1 == 0:
            print(word)


s = " i am vinay"
printWords(s)
