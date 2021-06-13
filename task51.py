from check_simple import simple_a

b = simple_a(1000000)

# Визначає кількість перестановок
def changer(n,sshelve,a):
    if n != []:
        for i in n:
            n2 = n[:]
            n2.remove(i)
            sshelve1 = sshelve
            sshelve1 += str(i)
            changer(n2,sshelve1,a=a)
            #print(1)
    else:
        a.append(sshelve)


def changer_number(n):
    #global res
    list = [int(i) for i in str(n)]
    res1 = []
    changer(list,'',a = res1)
    for i in res1:
        res_a = res1[:]
        res_a.remove(i)
        if i in res_a:
            res1 = res_a
    return res1

#Вибирає індикси по яких потрібно робити перебір
def convert(number):
    c = 0
    shelve = []
    for i in number:
        if i == '1':
            shelve.append(c)
        c+=1
    return shelve

convert_list_A = []# Список всіх можливих індексів по яких можна робити перебір до 6 чисел;len(max[...,...,... ...,...]) <=6
"""for i in range(1,6):
    u = '1'+'1'*(i-1) + '0'*(5-i)
    for i in changer_number(u):
        convert_list_A.append(convert(i))
"""
u = '111' + '00'
for i in changer_number(u):
    convert_list_A.append(convert(i))

def sum_a(number):
    s = 0
    for i in str(number):
        s+=int(i)
    return s
def result(i):

        length = len(str(i))
        if length == 6:
            '''for j in range(1, length):
                value = '1'*j + '0'*(length-j)
                list_variant = changer_number(int(value))
                for lip in list_variant:
                    convert_list = convert(lip)
                    #print(convert_list)'''
            for convert_list in convert_list_A:
                triple = ''
                for i1 in range(0,5):
                    if i1 not in convert_list:
                        triple +=str(i)[i1]

                if len(convert_list) < length and sum_a(int(triple)) % 3 != 0:
                    c = 0
                    k = 0
                    list_ar =[]
                    #if convert_list[0] != 0:
                    for hip in range(0, 10):
                        number = list(str(i))
                        for l in convert_list:
                            number[l] = str(hip)

                        prime_must_be = ''
                        for letter in number:
                            prime_must_be += letter
                        #print(prime_must_be)
                        if int(prime_must_be) in b:
                            c+=1
                            #print(c)
                            list_ar.append(prime_must_be)
                        else:
                            k +=1
                        if c == 8 and list_ar[0][0] != '0':
                            return list_ar
                        if k == 3:
                            break




for prime in b:
        if result(prime):
            print(result(prime))
            break
