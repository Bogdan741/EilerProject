'''Число 1406357289, является пан-цифровым, поскольку оно состоит из цифр от 0 до 9 в определенном порядке. Помимо этого, оно также обладает интересным свойством делимости подстрок.

Пусть d1 будет 1-ой цифрой, d2 будет 2-ой цифрой, и т.д. В таком случае, можно заметить следующее:

d2d3d4=406 делится на 2 без остатка
d3d4d5=063 делится на 3 без остатка
d4d5d6=635 делится на 5 без остатка
d5d6d7=357 делится на 7 без остатка
d6d7d8=572 делится на 11 без остатка
d7d8d9=728 делится на 13 без остатка
d8d9d10=289 делится на 17 без остатка
Найдите сумму всех пан-цифровых чисел из цифр от 0 до 9, обладающих данным свойством.'''

import re
import time
def grim(file):
    line1 = re.sub('0(?=\d)', '', file)
    #line2 = re.sub('\n', '', line1)
    return int(line1)


"""def changer(n,sshelve,a=[]):
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
    for i in res1:
        res_a = res1[:]
        res_a.remove(i)
        if i in res_a:
            res1 = res_a
    return res1
t1 = time.time()
list_variant = changer_number(12345678)

list_check_variant = check_simple.simple_a(17)
sum = 0
for i in list_variant:
    for j in range(1,7):
        isprost = str(i)[j:j+3]
        if grim(isprost) % list_check_variant[j-1] == 0:
            c = 1
            continue
        else:
            c = 0
            break
    if c:
        sum += i
t2 = time.time() - t1
print(sum,t2)"""


'''It is work...... But too long you must waiting for result......4+ hours...perhaps'''
t1 = time.time()
a = ['1','2','3','4','5','6','7','8','9','0']
b = [2,3,5,7,11,13,17]
res=[]

def loko_number_pan_abo_propan(listc, shelve='', index=0):
    if len(shelve) > 3:
        if grim(shelve[index+1:index+4]) % b[index] == 0:
            index1 = index + 1
            if len(shelve) == 10:
                return res.append(shelve)
            else:
                for value in listc:
                    shelve1 = shelve + value
                    listc1 = listc[:]
                    listc1.remove(value)
                    loko_number_pan_abo_propan(listc1, shelve=shelve1, index=index1)
        #else:
            #res.append("0")
    else:
        for value in listc:
            shelve1 = shelve + value
            listc1 = listc[:]
            listc1.remove(value)
            loko_number_pan_abo_propan(listc1, shelve=shelve1, index=index)
loko_number_pan_abo_propan(a)

a1 = [int(i) for i in res if i.isdigit()]
#print(a1)
sum = 0
for i in a1:
    sum+=i
t2 = time.time() - t1
print(sum,t2)  #Hoooooooh..... everything okay


