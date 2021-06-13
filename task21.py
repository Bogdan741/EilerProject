"""
Пусть d(n) определяется как сумма делителей n (числа меньше n, делящие n нацело).
Если d(a) = b и d(b) = a, где a ≠ b, то a и b называются дружественной парой, а каждое из чисел a и b - дружественным числом.

Например, делителями числа 220 являются 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 и 110, поэтому d(220) = 284. Делители 284 - 1, 2, 4, 71, 142, поэтому d(284) = 220.

Подсчитайте сумму всех дружественных чисел меньше 10000.

"""

import math

list_dilnyk_ch = []

def d(a):
    res=[1]
    for i in range(2,math.floor(math.sqrt(a))+1):
        if a % i ==0:
            res.append(i)
            res.append(a/i)
    sum = 0
    for s in res:
        sum+=s
    return sum
def final(n):
    sum = 0
    list_friend_n = []
    for a in range(n):
        if d(d(a)) == a:
            if a not in list_friend_n and d(a) not in list_friend_n:
                list_friend_n.append(a)
                list_friend_n.append(d(a))
    for i in list_friend_n:
        sum+=i

    return sum
print(final(10000))
print(d(25))



