import re
def dob(n,posl):
    j = 0
    k = n
    res = []
    def g():
        nonlocal k
        nonlocal j
        lich = 1
        for i in posl[j:k]:
            lich *= int(i)
        res.append(lich)
        k += 1
        j += 1
        if k <= len(posl):
            g()
    g()
    return max(res)


posl=''
tas8 = open('C:\python\Learn_python\myfile.txt')
for line in tas8:
    posl+=re.sub("^\s+|\n|\r|\s+$", '', line)
print(dob(13,posl))


