a=input('enter any number:')
sum=0
length_a=len(a)
for i in range(0,3):
    digit=a[0]
    sum=sum+(digit)**3
if (int(a))==sum:
    print('armstrong')
