import math
'''
Дозволяє знайти всі дільники даного числа 
'''


def d(a):
    res=[1]
    for i in range(2,math.floor(math.sqrt(a))+1):
        if a % i == 0:
            if i != a/i:
                res.append(i)
                res.append(a/i)
            else:
                res.append(i)
    res = [int(i) for i in res]
    return res


if __name__ == '__main__':
    print(d(19451945))