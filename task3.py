import math

def simple1(arg):
    k = False
    for i in range(2,arg):
        if arg%i == 0:
            k = False
            break
        else:
            k = True
    if k :
        return True

"""def parne(arg):
    if arg%2 == 0:
        arg = arg/2
        parne(arg)
    else:
        return arg
    
def D_on_three(arg):
    s=0
    arg = str(arg)
    for i in arg:
        s+=int(i)
"""
res=[]
def prostD(a):
    for i in range(3,math.floor(a+1), 2):
        if a%i == 0:
            if simple1(i):
                res.append(i)
                print(i)
                a = a/i
                break
    if a != 1:
        prostD(a)
    else:
        print('the end')
    return res
print(prostD(600851475143))
