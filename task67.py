from fichaE import grim
train = open(r'C:\Users\bodan\PycharmProjects\ProjectsE\task67(textfile)')
res = grim(train)# Convert file in list and del '0,\n....'

sums=[]
row_index = 0
for row in res:
    row_sums = []
    value_index = 0
    for value in row:
        value_sums = []
        previous_row_index = row_index - 1
        previous_left_value_index = value_index - 1
        previous_right_value_index = value_index

        if previous_row_index < 0:
            value_sums.append(value)

        else:
            previous_sum = []
            if previous_left_value_index >= 0:
                s = sums[previous_row_index][previous_left_value_index]
                previous_sum +=s
            if previous_right_value_index < len(sums[previous_row_index]):
                s = sums[previous_row_index][previous_right_value_index]
                previous_sum +=s
            max_v = 0
            for value1 in previous_sum:
                value1 += value
                max_v = max(max_v,value1)
            value_sums.append(max_v)
        if len(value_sums) > 0:
            row_sums.append(value_sums)
        value_index += 1
    sums.append(row_sums)
    row_index +=1
max_sum = 0
for rows in sums:
    for value in rows:
        for s in value:
           max_sum = max(max_sum,s)

if __name__ == '__main__':
    print(max_sum)