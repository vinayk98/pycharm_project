x = str(input('enter a string:'))
w = ""
for i in x:
    w = i + w
    if x == w:
        print('YES!string is a palindrome ')
    else:
        print('not a palindrome')