'''Дана иррациональная десятичная дробь, образованная объединением положительных целых чисел:

0.123456789101112131415161718192021...

Видно, что 12-ая цифра дробной части - 1.

Также дано, что dn представляет собой n-ую цифру дробной части. Найдите значение следующего выражения:'''

s = '0'
i = 0

while len(s) < 10**6+1:
    i += 1
    s += str(i)

sum = 1
for j in range(0,7):
    #print(s[10**j])
    sum *= int(s[10**j])

print(sum)
