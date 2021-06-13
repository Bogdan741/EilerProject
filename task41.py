'''Будем считать n-значное число пан-цифровым, если каждая из цифр от 1 до nиспользуется в нем ровно один раз. К примеру, 2143 является 4-значным пан-цифровым числом, а также простым числом.

Какое существует наибольшее n-значное пан-цифровое простое число?'''
from check_simple import simple_a
import task35
import time

shelve = []
k = [1234,1234567]# (123,12345,123456,12345678,123456789)%3 == 0, becouse the sum of number % 3
simple_list = simple_a(10**7)
t1 = time.time()
for i in k:
    for value in task35.changer_number(i):
        if value in simple_list:
            shelve.append(value)
if __name__ == '__main__':
    t2 = time.time() - t1
    print('The result: {0}\ntime: {1}'.format(max(shelve),t2))