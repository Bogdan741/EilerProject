def colattc(n):
    i = 0
    while True:
        i+=1
        if n == 1:
            break
        elif n % 2 ==1:
            n = 3*n+1
        elif n % 2 ==0:
            n = n/2
    return i
res={}
for i in range(2,1000000):
    res[colattc(i)] = i

print(max(res),res[max(res)])



