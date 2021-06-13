'''Перевірка на просість.Дозволяє з геренерувати список простих чисел до n за допомогою решета Ератосфена'''
from time import time
t = time()
def simple(n):
    lst = [2]
    for i in range(3, n+1, 2):
        if i > 10 and i % 10 == 5:
            continue
        for j in lst:
            if j*j-1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst

def simple_a(n):#the best
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
    return lst


'''Algoritm Evklida'''
def gcd(a, b):
    while True:
        if b > a:
            a, b = b, a
        a = a - b
        if b == a:
            return b
        if b == 0:
            return a


if __name__ == '__main__':
    print(simple_a(1000))
    ti = time() - t


