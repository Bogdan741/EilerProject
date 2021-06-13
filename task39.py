"""Если p - периметр прямоугольного треугольника с целочисленными длинами сторон {a,b,c}, то существует ровно три решения для p = 120:

{20,48,52}, {24,45,51}, {30,40,50}

Какое значение p ≤ 1000 дает максимальное число решений?"""

import time
def directly_triangle(a,b,c):
    if a**2 == c**2 + b**2:
        return True

def inter(p):
    count = 0
    res = []
    for a in range(1,int(p/2)+1):
        for b in range(1, int(p/2)+1):
            c = p - (a + b)
            if b > c and c != 0:
                if directly_triangle(a,b,c):
                        #res.append(a)
                        #res.append(b)
                        #res.append(c)
                    count+=1
                    #print(a,b,c)

    return count
t1 = time.time()
s=0
for i in range(10,1000):
    l = inter(i)
    if s < l:
        s = l
t2 = time.time() - t1
print(s,t2)
if __name__ == '__main__':...
    #print(directly_triangle(3,4,5))
    #print(inter(1000))
