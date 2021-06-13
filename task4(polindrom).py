def polindrom(a):
    s=''
    for i in str(a)[::-1]:
        s+=i
    s = int(s)
    if a == s:
        return 1


def check_pol(a):
    res = []
    beg = '1'+'0'*(a-1)
    beg = int(beg)
    fin = '9'*a
    fin = int(fin)
    for i in range(beg, fin+1):
        for j in range(beg, fin+1):
            s = i*j
            if polindrom(s):
                res.append((i*j))
                #print(i, j)
    print(max(res))
check_pol(4)