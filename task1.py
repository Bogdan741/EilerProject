max=1000
S1=0
for i in range((max//3)+1):
    S1+=i*3
S2=0
for i in range((max//5)+1):
    S2+=i*5
print(S1+S2)