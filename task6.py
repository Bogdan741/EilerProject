def square(n):
    substracting = (n**2*(n+1)**2/4) - (n*(n+1)*(2*n+1)/6)
    return substracting
print(square(100))