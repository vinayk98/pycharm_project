import calculator2
op=input('operator:')
a,b=int(input("a:")),int(input("b:"))
print(calculator2.calulator.dict[op](a,b))