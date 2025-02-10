# map(function,iterable object) ---> Iterator object

def double(x):
    return x*2

li =[1,2,3,4]
double_li =list(map(double,li))
print(double_li)


tup = ('10','20','30')
print(tup)
tuple = tuple(map(int,tup))
print(tuple)