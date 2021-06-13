"""Пятиугольные числа вычисляются по формуле: Pn=n(3n−1)/2. Первые десять пятиугольных чисел:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

Можно убедиться в том, что P4 + P7 = 22 + 70 = 92 = P8. Однако, их разность, 70 − 22 = 48, не является пятиугольным числом.

Найдите пару пятиугольных чисел Pj и Pk, для которых сумма и разность являются пятиугольными числами и значение D = |Pk − Pj| минимально, и дайте значение D в качестве ответа."""
import time
"""i = 1
res = []
c = 1
while c:
    P = i*(3*i - 1)/2
    res.append(P)
    if len(res) >1000:
        break
    if len(res) > 3:
        res1 = res[:]
        for p1 in res:
            res1.remove(p1)
            for p2 in res1:
                if (p2 - p1) in res and (p2 + p1) in res:
                    print(p2 - p1)
                    c = 0
                    break
                else:
                    continue
    i+=1"""
t1 =time.time()
a = [i*(3*i - 1)/2 for i in range(1000,10000)]


def p():
    a1 = a[:]
    if len(a) > 3:
        for pi in a:
            a1.remove(pi)
            for pk in a1:
                if ((pk - pi) in a or (pi - pk) in a) and (pi + pk) in a:
                    return pk - pi



print(p())
t2 = time.time() - t1
print(t2)

