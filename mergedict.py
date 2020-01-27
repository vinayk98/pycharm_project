"""
discripsion about the program,
this program merge two dictionaries
"""
a={"a":1,"b":2,"c":3}
b={"d":5,"e":10,"f":11}
all_keys=list(a.keys())+list(b.keys())
all_values=list(a.values())+list(b.values())
result={**a,**b}
# for keys,values in zip(all_keys,all_values):
#     result.update({keys:values})'
# lkhlsjcacasljkhdvj

print(result)