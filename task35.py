"""
Число 197 называется круговым простым числом, потому что все перестановки его цифр с конца в начало являются простыми числами: 197, 719 и 971.

Существует тринадцать таких простых чисел меньше 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79 и 97.

Сколько существует круговых простых чисел меньше миллиона?

"""
import check_simple
from factorial import factorial
res =[]
def changer(n,sshelve,a=[]):
    if n != []:
        for i in n:
            n2 = n[:]
            n2.remove(i)
            sshelve1 = sshelve
            sshelve1 += str(i)
            changer(n2,sshelve1,a=a)
            #print(1)
    else:
        a.append(sshelve)


def changer_number(n):
    #global res
    list = [int(i) for i in str(n)]
    res1 = []
    changer(list,'',a = res1)
    res1 = [int(i) for i in res1]
    for i in res1:
        res_a = res1[:]
        res_a.remove(i)
        if i in res_a:
            res1 = res_a
    return res1



a_a = check_simple.simple_a(10**6)
#a_a = [2,3,5,7,11,13,17,31,37,71,73,79,97]
count = 0
list_anon = []
"""for i in range(3,10**5,2):#first version
    k = len(changer_number(i))
    for number in changer_number(i):
        if i in list_anon:
            c = 0
            break
        else:
            if number in a_a:
                c = 1
                continue
            else:
                c = 0
                break
    if c:
        count+=factorial(k)
        for number in changer_number(i):
            list_anon.append(number)
"""
def _count(list):#second version(the best)
    global count
    for a in a_a:
        list_variant = changer_number(a)
        for lis in list_variant:
            if lis in a_a:
                c = 1
                continue
            else:
                c = 0
                break
        if c == 1:
            for i in list_variant:
                a_a.remove(i)
            count+=factorial(len(list_variant))
            _count(a_a)
if __name__ == '__main__':
    #_count(a_a)
    #print(count)
    print((changer_number(1234)))




