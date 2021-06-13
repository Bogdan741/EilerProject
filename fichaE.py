import re
def grim(file,convert_func = int):
    l =[]
    for line in file:
        line1 = re.sub('0(?=\d)', '', line)
        line2 = re.sub('\n', '', line1)
        val = [convert_func(s) for s in line2.split(' ')]
        l.append(val)
    return l

if __name__ == '__main__':
    train = open(r'C:\Users\bodan\PycharmProjects\ProjectsE\task18(textfile)')
    print(grim(train))