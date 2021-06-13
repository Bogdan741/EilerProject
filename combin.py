from factorial import factorial
import math
sum=0
for i in range(0,11):
    sum+=4**i/factorial(i)*math.exp(-4)
print(sum)