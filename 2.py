def rev(x):
    y = ""
    for i in x:
       y = i + y
    return y

z = rev(['4','1','2','9'])
print(z)