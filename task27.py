"""Эйлер опубликовал свою замечательную квадратичную формулу:

n**2+n+41
Оказалось, что согласно данной формуле можно получить 40 простых чисел, последовательно подставляя значения 0≤n≤39. Однако, при n=40, 402+40+41=40(40+1)+41 делится на 41 без остатка, и, очевидно, при n=41,412+41+41 делится на 41 без остатка.

При помощи компьютеров была найдена невероятная формула n2−79n+1601, согласно которой можно получить 80 простых чисел для последовательных значений n от 0 до 79. Произведение коэффициентов −79 и 1601 равно −126479.

Рассмотрим квадратичную формулу вида:

n**2+an+b, где |a|<1000 и |b|≤1000

где |n| является модулем (абсолютным значением) n.
К примеру, |11|=11 и |−4|=4
Найдите произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное количество простых чисел для последовательных значений n, начиная со значения n=0.
"""


def simple_number(n):
    lst = [2]
    for i in range(3, n + 1, 2):
        if i > 10 and i % 10 == 5:
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


dictionary_correct = {}

for a in range(3,1000,2):
    for b in simple_number(1000):
        if a**2 - 4*b < 0:
            n = 0
            while True:
                k = n**2 + a*n + b
                if k in simple_number(k):
                    n+=1
                    continue
                else:
                    dictionary_correct[n] = a*b
                    break


for a in range((-3), (-1000), -2):
    for b in simple_number(1000):
        if a**2 - 4*b < 0:
            n = 0
            while True:
                k = n**2 + a*n + b
                if k in simple_number(k):
                    n+=1
                    continue
                else:
                    dictionary_correct[n] = a*b
                    break

number = 0
for s in dictionary_correct:
    if number < s:
        number = s
print(dictionary_correct[number],number)


"""You can check your understanding with notebook, key = 26"""