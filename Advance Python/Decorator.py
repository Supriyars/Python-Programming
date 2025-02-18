def decor(func):
    def inner(name):
        if name == 'Ayush':
            print(name,'Is Learning Java')
        else:
            func(name)
    return inner
@decor
def choice (name):
    print(name, 'Is learning Python')
choice('Ayush')
choice('Akash')
 



 