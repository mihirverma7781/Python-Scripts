def ex(num,*args):
    li=[(i**num) if args else "you did'nt pass anything" for i in args ]
    return li
m=[2,3]
print(ex(2,*m))