"""Арифметическая прогрессия: 1487, 4817, 8147, в которой каждый член возрастает на 3330, необычна в двух отношениях: (1) каждый из трех членов является простым числом, (2) все три четырехзначные числа являются перестановками друг друга.

Не существует арифметических прогрессий из трех однозначных, двухзначных и трехзначных простых чисел, демонстрирующих это свойство. Однако, существует еще одна четырехзначная возрастающая арифметическая прогрессия.

Какое 12-значное число образуется, если объединить три члена этой прогрессии?"""

import check_simple

def separate(n):
    number_digit = str(n)
    shelve = []
    for i in number_digit:
        shelve.append(int(i))
    shelve.sort()
    return shelve

varianta_simple = [i for i in check_simple.simple_a(10**5) if len(str(i)) == 4]

res = []

for i in varianta_simple:
    res.append((i,separate(i)))

list_check = []
rubbish = []
for i in res:
    z = i[1]
    c = 0
    shelve = []
    if z not in rubbish:
        for j in res:
            if j[1] == z:
                c += 1
                shelve.append(j[0])
        if c >= 3:
            list_check.append(shelve)
        rubbish.append(z)



for i in list_check:
    k=0
    for j in i:
        k+=1
        k1 = k
        for j1 in i[k:]:
            k1+=1
            if j1 != j:
                for j2 in i[k1:]:
                    if j2 != j1 and j2 != j:
                        if (j+j1+j2)/3 in [j,j1,j2] and j2 - j1 == j1 - j:
                            print([j,j1,j2])









