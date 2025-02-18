def smartdiv(func):
    def inner(a,b):
        if b == 0:
            print('b Should not be 0')
        else:
            func(a,b)
    return inner
@smartdiv
def div(a,b):
    print('Division is:', a/b)
div(10,2)
div(2,0)