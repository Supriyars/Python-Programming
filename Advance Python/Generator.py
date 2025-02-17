#def disp():
    #return 10
    #return 20
    #return 30
#print(disp()) #10
#print(disp()) #10

def generator_function():
    print('One')
    yield 10
    print('Two')
    yield 20
    print('Three')
    yield 30
print(generator_function())
ref = generator_function()
print(next(ref))
print(next(ref))
print(next(ref))