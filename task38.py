"""Возьмем число 192 и умножим его по очереди на 1, 2 и 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
Объединяя все три произведения, получим девятизначное число 192384576 из цифр от 1 до 9 (пан-цифровое число). Будем называть число 192384576 объединенным произведением 192 и (1,2,3)

Таким же образом можно начать с числа 9 и по очереди умножать его на 1, 2, 3, 4 и 5, что в итоге дает пан-цифровое число 918273645, являющееся объединенным произведением 9 и (1,2,3,4,5).

Какое самое большое девятизначное пан-цифровое число можно образовать как объединенное произведение целого числа и (1,2, ... , n), где n > 1?"""

def is_pan(number):
    inter = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
    if 10**8 <= number < 10**9:
        for i in str(number):
            if int(i) in inter:
                inter.remove(int(i))
                continue
            else:
                c = 0
                return False
    else:
        return False
    return True
'''def pan_number(n):
    k = len(str(n))
    inter1 = list(range(1,k+1))
    for i in str(n):
        if int(i) in inter1:
            inter1.remove(int(i))
            continue
        else:
            return False
    return True'''

"""Obviously that the sequence must be larger and larger, step by step, but we should compete a same number with bigger n, so the finded number is more the 1 and lover then 99."""
res = []
def sequence_check(number, cash='', step = 1):
    if len(cash) == 9:
        res.append(int(cash))
    elif len(cash) > 9:
        ...
    else:
        cash1 = cash + str(number * step)
        step1 = step + 1
        sequence_check(number, cash = cash1, step = step1)

for i in range(1,1000):
    sequence_check(i)

res = [i for i in res if is_pan(i)]
print(max(res))