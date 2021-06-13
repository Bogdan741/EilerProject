import math

def simple1(n):  # перевівка на простість
    lst = [2]
    for i in range(3, n + 1, 2):
        if i > 10 and i % 10 == 5:
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)
    if n in lst:
        return True
    else:
        return False


"""def prostDL(arg1):  # виводить список простих дыльників числа а(основа розв"язку)
    res = []

    def parne(arg1):  # perevirka na parnist(складова перевірки на простість)
        if arg1 % 2 == 0 :
            arg1 = int(arg1 / 2)
            res.append(2)
            return parne(arg1)
        else:
            return arg1
    arg1 = parne(arg1)

    def prostD(arg1):
        for i in range(3, math.floor(arg1 + 1), 2):
            if arg1 % i == 0:
                if simple1(i):
                    res.append(i)
                    # print(i)
                    arg1 = arg1 / i
                    prostD(arg1)



    if arg1 != 1:
        prostD(arg1)
    return res"""


def prostDL(arg):
    res = []
    while arg % 2 == 0:
        arg = arg / 2
        res.append(2)
    def a(arg):
        i = 3
        val = arg
        while True:
            if i<=val:
                if val % i == 0 and simple1(i):
                    res.append(i)
                    val = val/i
                    i=1
                i+=2
            else:
                break
    a(arg)
    return res
if __name__ == '__main__':
    print(prostDL(4945191))