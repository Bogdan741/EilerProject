"""
Пусть r будет остатком от деления (a−1)n + (a+1)n на a2.

К примеру, если a = 7 и n = 3, то r = 42: 63 + 83 = 728 ≡ 42 mod 49. При изменении n будет изменяться и r, однако, для a = 7 оказывается, что rmax = 42.

Найдите ∑ rmax для 3 ≤ a ≤ 1000.
"""
import math
sum = 0
for a in range(3, 1001):
    remainders = 2
    for n in range(1, math.floor(a/2)+2):
        c = 2*n*a % a**2
        if c > remainders:
            remainders = c
    sum += remainders

print(sum)
#333082500