class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)


#@tracer # То же, что и spam = tracer(spam)
def spam(a, b, c): # Обертывает spam в объект-декоратор
    print (a, b, c)
spam = tracer(spam)
spam(1, 2, 3) # В действительности вызывается объект-обертка # То есть вызывается метод __call__ в классе
spam(4, 5, 6)