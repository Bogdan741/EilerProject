"""import math

def factorial(n):
    s=1
    for i in range(1,n+1):
        s*=i
    return s

def prostDL(a):#виводить список простих дыльників числа а(основа розв"язку)
    res=[]
    def parne(a):  # perevirka na parnist(складова перевірки на простість)
        if a % 2 == 0 :
            a = int(a / 2)
            res.append(2)
            return parne(a)
        else:
            return a
    a = parne(a)
    def prostD(a):
        for i in range(3,math.floor(a+1), 2):
            if a%i == 0:
                if simple1(i):
                    res.append(i)
                    #print(i)
                    a = a/i
                    break
        if a != 1:
            prostD(a)
        #else:
            #print('the end')
        #return res
    if a!=1:
        prostD(a)
    return res


def simple1(n):
    a = list(range(n+1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    if n in lst:
        return True

print(prostDL(944))


i=0
while True:
    i+=1
    n = int(i*(i+1)/2)
    k=prostDL(n)
    sum = factorial(len(k)-1)
    print(k)
    if sum >=500:
        print(n)
        break"""

import math
from time import time
t = time()
def divisors(n):
       number_of_factors = 1
       for i in range(2, int(math.ceil(math.sqrt(n)))):
           if n % i == 0:
               number_of_factors +=2
           else:
               continue
       return number_of_factors

x=1
for y in range(2,1000000):
       x += y
       if divisors(x) >= 500:
           print (x)
           break
tt = time()-t
print (tt)



