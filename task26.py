"""Единичная дробь имеет 1 в числителе. Десятичные представления единичных дробей со знаменателями от 2 до 10 даны ниже:

1/2	=	0.5
1/3	=	0.(3)
1/4	=	0.25
1/5	=	0.2
1/6	=	0.1(6)
1/7	=	0.(142857)
1/8	=	0.125
1/9	=	0.(1)
1/10	=	0.1
Где 0.1(6) значит 0.166666..., и имеет повторяющуюся последовательность из одной цифры. Заметим, что 1/7 имеет повторяющуюся последовательность из 6 цифр.

Найдите значение d < 1000, для которого 1/d в десятичном виде содержит самую длинную повторяющуюся последовательность цифр."""
from prost_dl import prostDL
from time import time
from check_simple import simple_a
res_op = []

def p(number):
    res_opos = []
    for value in prostDL(number):
        if value in res_opos:
            continue
        else:
            res_opos.append(value)
    return res_opos

"""def count_repeted(n, rest=1, shelve=''):
    #if p(n) == [2,5] or p(n) == [2] or p(n) == [5]:
        #return res_op.append((n,0))
    while True:
        if rest // n == 0:
            rest = rest * 10
        else:
            rest, shelve = rest - n*(rest // n ), shelve + str(rest//n)
            break

    k = len(shelve) // 2
    if shelve[:k] == shelve[k:] and k != 0:
        return res_op.append((n,k))
    else:
        count_repeted(n, rest=rest, shelve=shelve)
"""
def count_repeted(n, rest=1, shelve=''):
    while True:
        k = len(shelve) // 2
        if shelve[:k] == shelve[k:] and k != 0:
            return res_op.append((n, k))
        if rest // n == 0:
            rest = rest * 10
        else:
            rest, shelve = rest - n*(rest // n ), shelve + str(rest//n)
t1 = time()

for i in simple_a(1000):
    if i != 2 and i != 5:
        count_repeted(i)



lich = 0
li=0
for seq in res_op:
    if seq[1] > lich:
        lich = seq[1]
        li = seq[0]
t2 = time() - t1
print(lich,li,t2,sep = '\n')
























