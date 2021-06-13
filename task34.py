"""
145 является любопытным числом, поскольку 1! + 4! + 5! = 1 + 24 + 120 = 145.

Найдите сумму всех чисел, каждое из которых равно сумме факториалов своих цифр.

Примечание: поскольку 1! = 1 и 2! = 2 не являются суммами, учитывать их не следует.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


sum_list = 0
for i in range(10,100000):
    number = str(i)
    sum = 0
    for var in number:
        var1 = int(var)
        sum += factorial(var1)
    if sum == i:
        sum_list += i
print(sum_list)