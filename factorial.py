def factorial(n):
    if n ==0:
        return 1
    else:
        sum = 1
        for i in range(1,n+1):
            sum*=i
        return sum




def simple_a(n):#the best
    a = list(range(n+1))
    a[1] = 0

    lst = []
    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    return lst

"""def prostDL(arg):
    simpleU = simple_a(arg)
    res = []
    while arg % 2 == 0:
        arg = arg / 2
        res.append(2)
    def a(arg):
        i = 0
        val = arg
        while True:
            if simpleU[i]<=val:
                if val % simpleU[i] == 0:
                    res.append(simpleU[i])
                    val = val/simpleU[i]
                    i=0
                i+=1
            else:
                break
    a(arg)
    return res"""