#кожне число розклаємо на прості множника
#беромо прості множники з кожного числа у виді словника де ключ це просте число а значення його кількість.
# Вибираємо кожне просте число найвищої степені і подаємо добуток всіх

import math

def simple1(arg):#перевівка на простість
    for i in range(2,arg):
        if arg%i == 0:
            break
    else:
        return True


def prostDL(a):#виводить список простих дыльників числа а(основа розв"язку)
    res=[]


    def parne(a):  # perevirka na parnist(складова перевірки на простість)
        if a % 2 == 0 :
            a = int(a / 2)
            res.append(2)
            return parne(a)
        else:
            return a
    arg1 = parne(a)


    def prostD(arg1):
        for i in range(3,math.floor(arg1+1), 2):
            if arg1%i == 0:
                if simple1(i):
                    res.append(i)
                    #print(i)
                    arg1 = arg1/i
                    break
        if arg1 != 1:
            prostD(arg1)
        #else:
            #print('the end')
        #return res
    if arg1!=1:
        prostD(arg1)
    return res


def dictionaryC(a):
    a1 = {}
    for i in range(a+1):
        if simple1(i):
            if i in prostDL(a):
                a1[i] = prostDL(a).count(i)

    return a1


def NSK(a):
    S = 1
    for j in range(2,a+1):#проводить кінуевий аналіз
        if simple1(j):
            res = []
            for i in range(2,a+1):
                if j in dictionaryC(i).keys():
                    res.append(dictionaryC(i)[j])

            S = S*j**max(res)
    print(S)
#NSK(100)
print(prostDL(220))