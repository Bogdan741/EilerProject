class TraceBlock:
    def message(self, arg):
        print('running', arg)
    def __enter__(self):
        print('starting with block')
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('raise an eception', exc_type)
            return False

with TraceBlock() as action:
    action.message('test1')
    print('reached')

with TraceBlock() as action:
    action.message('test2')
    raise TypeError
    print('not reachd')