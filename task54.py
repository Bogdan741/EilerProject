import re
import pickle
"""import and adjustment the information"""
list=[]
finale=[]
k = "9H 9D JD JH 3S AH 2C 6S 3H 8S \n"
with open('task54_text','r') as O:
    for i in O:
       list.append(i)
for i in list:
    m = re.sub('\n','',i).split(' ')
    finale.append(m)
print(finale[0])

"""main part"""
value_list={'2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            'T':10,
            'J':11,
            'Q':12,
            'K':13,
            'A':14}

