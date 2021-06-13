import time
class Date:
    def __init__(self,day,month,year,weekday):
        self.day = day
        self.month = month
        self.year = year
        self.weekday = weekday
    def monthda(self,i):
        if i%12 == 2:
            self.weekday = (self.weekday + 31%7)%7
        if i%12 == 3:
            if self.year%4 == 0:
                self.weekday = (self.weekday + 29%7)%7
            else:
                self.weekday = (self.weekday + 28%7)%7
        if i%12 == 4:
            self.weekday = (self.weekday + 31%7)%7
        if i%12 == 5:
            self.weekday = (self.weekday + 30%7)%7
        if i%12 == 6:
            self.weekday = (self.weekday + 31%7)%7
        if i%12 == 7:
            self.weekday = (self.weekday + 30%7)%7
        if i%12 == 8:
            self.weekday = (self.weekday + 31%7)%7
        if i%12 == 9:
            self.weekday = (self.weekday + 31%7)%7
        if i%12 == 10:
            self.weekday = (self.weekday + 30%7)%7
        if i%12 == 11:
            self.weekday = (self.weekday + 31%7)%7
        if i%12 == 12:
            self.weekday = (self.weekday + 30%7)%7
        if i%12 == 1:
            self.weekday = (self.weekday + 31%7)%7
        return self.weekday
dayW = {1:'Monday',
        2:'Tuesday',
        3:'Wednesday',
        4:'Thursday',
        5:'Friday',
        6:'Saturday',
        0:'Sunday'}
x = Date(1,1,1901,1)
#print('1:{}'.format(dayW[x.monthda()]))
i = x.month+1
count=0
t1 = time.time()
while True:
    if x.monthda(i) == 0:
        count+=1
    i+=1
    if i == 13:
        i = 1
        x.year+=1
    if x.year == 2001:
        break

print(count)
ti = time.time() - t1
print(ti)


