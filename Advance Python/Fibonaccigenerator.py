def fibonacci_gen(num):
    a, b = 0,1
    for i in range (num):
        yield a
        a,b = b, a+b
ref = fibonacci_gen(10)
print(next(ref))
print(next(ref))

#or i in ref:
   # print(i)