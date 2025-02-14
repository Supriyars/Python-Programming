class Demo1:
    def __str__(self):
       return 'Hello'
    def __add__(self,other):
        self.a = 20
        self.b = 30
        return self.a + other.b 
class Demo2:
    def __str__(self):
       return 'Hi'
d1 = Demo1()
d2 = Demo2()
print(d1)
print(d2)
print(d1+d2)

'''
Dunder methods : The methods which has suffix and prefix  as __(double underscore)
These dunder methods can be called as "magic mthods" because as programmer 
we no need to call any methods, automatically methods will be invoked. 
'''
'''
In python if we trying to print reference variable then  internally python will invoke t
__str__() dunder method which will  always return string representation of an address of an object.

In the above examples we have overridden __str__ () method in their respective classes...
 '''