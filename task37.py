'''Число 3797 обладает интересным свойством. Будучи само по себе простым числом, из него можно последовательно выбрасывать цифры слева направо, число же при этом остается простым на каждом этапе: 3797, 797, 97, 7. Точно таким же способом можно выбрасывать цифры справа налево: 3797, 379, 37, 3.

Найдите сумму единственных одиннадцати простых чисел, из которых можно выбрасывать цифры как справа налево, так и слева направо, но числа при этом остаются простыми.

ПРИМЕЧАНИЕ: числа 2, 3, 5 и 7 таковыми не считаются.'''


from check_simple import simple_a
#print(simple_a(100))
from time import time

lis_may_number = [1, 3, 7, 9]


def function(list_n, n, shelve='', res=[]):
    if n != 0:
        for i in list_n:
            shelve1 = shelve + str(i)
            n1 = n - 1
            function(list_n, n1, shelve=shelve1, res=res)
    if n == 0:
        res.append(shelve)


def count_four(list_n, n):
    my_res = []
    function(list_n, n, res=my_res)
    my_res = [int(i) for i in my_res]
    return my_res

#print(count_four(lis_may_number, 6))
t1 = time()
count = 2
sum = 76#23+53
i = 2
while True:
    if count >= 11:
        break
    else:
        valueL = [i for i in count_four(lis_may_number,i) if i in simple_a(i)]
        for value in valueL:
            for j in range(1, i):
                if (int(str(value)[:-j]) in simple_a(value) and
                    int(str(value)[j:]) in simple_a(value)):
                    c = 1
                    continue
                else:
                    c = 0
                    break
            if c == 1:
                count += 1
                sum += value
                print(value)
    i += 1
ti = time() - t1
print(sum, ti)

