from check_simple import simple_a
from time import time
t1 = time()
count = 0
sum = 0
i = 2
while True:
    if count >= 11 or i == 11:
        break
    else:
        k2 = i - 1
        valueL = [l for l in simple_a(10**i) if l > 10**k2]
        for value in valueL:
            for j in range(1, i):
                if (int(str(value)[:-j]) in simple_a(value) and int(str(value)[j:]) in simple_a(value)):
                    c = 1
                    continue
                else:
                    c = 0
                    break
            if c == 1:
                count += 1
                sum += value
                print(value)
    i += 1
t = time() - t1
print(sum,t)

