"""Каждое n-значное число, которое содержит каждую цифру от 1 до n ровно один раз, будем считать пан-цифровым; к примеру,
5-значное число 15234 является пан-цифровым, т.к. содержит цифры от 1 до 5.

Произведение 7254 является необычным, поскольку равенство 39 × 186 = 7254, состоящее из множимого, множителя и
произведения является пан-цифровым, т.е. содержит цифры от 1 до 9.

Найдите сумму всех пан-цифровых произведений, для которых равенство "множимое × множитель = произведение" можно записать
цифрами от 1 до 9, используя каждую цифру только один раз.

ПОДСКАЗКА: Некоторые произведения можно получить несколькими способами, поэтому убедитесь, что включили их в сумму лишь
единожды."""

import dilnyk_n

correct = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
sum = 0
for number in range(1000,10000):
    vanish = []
    for dilnyk in dilnyk_n.d(number):
        #if (len(str(dilnyk)) == 2 and len(str(number/dilnyk)) == 3 or
                #len(str(dilnyk)) == 3 and len(str(number / dilnyk)) == 2):
            if dilnyk not in vanish:
                list_correct_number = sorted([val1 for val1 in str(dilnyk)]
                                         + [val2 for val2 in str(int(number/dilnyk))]
                                         + [val3 for val3 in str(number)])
                if list_correct_number == correct:
                    sum += number
                else:
                    vanish.append(dilnyk)
                    vanish.append(int(number/dilnyk))
print(sum)
