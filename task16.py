"""2**15 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.

Какова сумма цифр числа 2**1000?"""
b = str(2**1000)
sun = 0
for a in b:
    sun += int(a)
print(sun)