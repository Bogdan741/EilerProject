def supernet(n):
    res = [1]
    for i in range(2,n+1):
        res_beta = [1]
        sum = 1
        if len(supernet(n-1)) != 1:
            for j in range(1,len(supernet(n-1))):
                sum = sum + supernet(n-1)[j]
                res_beta.append(sum)
        res_beta.append(sumnet(n-1))
        res = res_beta
    return res

def sumnet(n):
    sum = 1
    sumA = 1
    if n == 1:
        return 2
    if len(supernet(n-1)) >=2:
        for i in range(1,len(supernet(n-1))):
            sumA = sumA + supernet(n-1)[i]
            sum = sum + sumA
    return 2*(sum + sumnet(n-1))

print(sumnet(20))





