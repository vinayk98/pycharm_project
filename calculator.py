def add (a,b):
    return(a+b)
def subtract(a,b):
    return(a-b)
def multiply(a,b):
    return(a*b)
def divide(a,b):
    return(a/b)
calculator={"+":add,
           "-":subtract,
           "*":multiply,
           "/":divide,
           }
op=input("enter operator")
num=input("enter numbers")
x=[int(i) for i in num.split(",")]
print(calculator[op](x[0],x[1]))