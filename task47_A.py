import check_simple
simple = check_simple.simple_a(1000000)
def prostDL(arg):
    res = []
    while arg % 2 == 0:
        arg = arg / 2
        res.append(2)
    def a(arg):
        i = 0
        val = arg
        while True:
            if simple[i]<=val:
                if val % simple[i] == 0 and simple[i]:
                    res.append(simple[i])
                    val = val/simple[i]
                    i=0
                i+=1
            else:
                break
    a(arg)
    return res

number = int(input('Enter a number: '))





def prostDL_up(n):
    res = []
    check = []
    for i in prostDL(n):
        if i not in check:
            res.append(i**prostDL(n).count(i))
            check.append(i)
    return res

list_that_i_use = [(i,prostDL_up(i)) for i in range(99996,200000) if len(prostDL_up(i)) == number]
print(len(list_that_i_use))

k = number
while True:
    massive = list_that_i_use[k-number:k]
    s = 0
    count = 0
    for i in massive:
        if i[0] > s and s != 0:
            if i[0] == s+1:
                s = i[0]
                count += 1
                continue
            else:
                break
        else:
            s = i[0]

    if count == number-1:
        listC = []
        for i in massive:
            for j in i[1]:
                if j not in listC:
                    listC.append(j)
        if len(listC) == number**2:
            print(list_that_i_use[k - number:k])
            break

    if k == len(list_that_i_use):
        break
    k +=1



