n=int(input('enter any number:'))
next_n,sum=n,0
while next_n>0:
    digit=next_n%10
    sum=sum+(digit)**3
    next_n=next_n//10
if n==sum:
    print('armstrong number')