"""n! означает n × (n − 1) × ... × 3 × 2 × 1

Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Найдите сумму цифр в числе 100!."""


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


sum = 0
for s in str(factorial(10)):
    sum += int(s)
print(sum)