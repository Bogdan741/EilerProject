import re
import numpy as np
from myt import mysortd


train = open(r'C:\Users\bodan\PycharmProjects\ProjectsE\train')
s=''
for line in train:
    match = re.sub('0(?=\d)', '', line)
    match1 = re.sub('\n', ' ', match)
    s+=match1
resB=[]

k = s.split(' ')


for l in range(0,16):
    res = []
    for i in range(l,4+l):
        for i1 in range(l,4+l):
            res.append(k[i+20*i1])
    resB.append(res)

result=[]
for k in resB:
    res1 = np.array(k[:]).reshape(4, 4).transpose()
    result.append(mysortd(res1))
print(max(result))

