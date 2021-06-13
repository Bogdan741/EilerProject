import numpy as np
def mysortd(a,n=4):
    b=[]
    for i in range(0,n):
        s = 1
        for j in range(0,n):
            s = s * int(a[j][i])
        b.append(s)

    for i in range(0, n):
        s = 1
        for j in range(0,n):
            s=s * int(a[i][j])
        b.append(s)

    s1=1
    for i in range(0,n):
        for j in range(0,n):
            if i == j:
                s1 = s1 * int(a[i][j])
    b.append(s1)

    s2=1
    for i in range(0,n):
        for j in range(0,n):
            if i + j == n:
                s2 = s2 * int(a[i][j])
    b.append(s2)
    return max(b)
