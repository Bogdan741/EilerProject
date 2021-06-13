"""Кристиан Гольдбах показал, что любое нечетное составное число можно записать в виде суммы простого числа и удвоенного квадрата.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

Оказалось, что данная гипотеза неверна.

Каково наименьшее нечетное составное число, которое нельзя записать в виде суммы простого числа и удвоенного квадрата?"""
import check_simple
import math
import time
t1 = time.time()
list_s = check_simple.simple_a(10000)
a = [i for i in range(3,10000,2) if i not in list_s]

for value in a:
    #res = check_simple.simple_a(value)
    for tax in range(1,int(math.sqrt(value))):
        k = value - 2*tax**2
        if k in list_s:
            c = 0
            break
        else:
            c = 1
            continue
    if c:
        print(value)
        break
t2 = time.time() - t1
print(t2)