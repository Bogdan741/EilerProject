def factorial(n):
    sum=1
    for i in range(1,n+1):
        sum*=i
    return sum

def my_combinations(n,k):
    sum = 1
    for i in range(k+1,n+1):
        sum*=i
    sum = sum/factorial(n-k)
    return sum

def number(n):
    count=0
    for i in range(2,n+1):
        for j in range(1,n):
            if 10**6 > my_combinations(i,j):
                continue
            else:
                count+=(n-1)-2*(j-1)
                break
    return count
print(number(100))
