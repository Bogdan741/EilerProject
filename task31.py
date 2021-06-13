'''В Англии валютой являются фунты стерлингов £ и пенсы p, и в обращении есть восемь монет:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) и £2 (200p).
£2 возможно составить следующим образом:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p'''
import time
pences = (200, 100, 50, 20, 10, 5, 2, 1)
total = 0


def count(value, cash):
    global total
    for i in range(0, 201, pences[value]):
        if cash + i < 200 and value < 7:
            temp = count(value + 1, cash + i)
            total += temp
            #total += count(value + 1, part + i)
        elif cash + i == 200 or value == 7:
            return 1
        else:
            return 0


temp = count(0, 0)
#total += temp
#total += count(0, 0)
print('Ответ:', total)
print(time.process_time())