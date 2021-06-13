from task5 import simple1
print(simple1(5))
def pr(n):
    i=1
    n1=0
    while True:
        i+=2
        if simple1(i):
            n1+=1
        if n1 == n-1:
            break
    return i
print(pr(1000))


