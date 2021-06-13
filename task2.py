#Fibonachi

#massiveF = [x**2 for x in range(5) ]
"""res = []

def fib(n):
     a, b = 0, 1
     while a < n:
         res.append(a)
         T = a
         a = b
         b = b + T

fib(1000)
print(res)"""

res = [0,1]
def fib(n):
    while True:
        a = res[-1]+res[-2]
        if a > n:
            break
        res.append(a)

fib(1000)
final = [i for i in res if i%2==0]
print(final)