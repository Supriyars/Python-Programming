from abc import ABC ,abstractmethod
class Demo1(ABC):
    @abstractmethod
    def disp1(self):
        print('Inside disp1 method')
d1 = Demo1() #This is not allowed gives error
'''
if abstract class does not have any method
then object for that abstract class can be created...
'''
class Demo2:
    def disp2(self):
        print('Inside disp2')
d2 = Demo2()
print(d2) #This is allowed

class Demo3(ABC):
    def info(self):
        print('Inside info')
    @abstractmethod
    def disp3(self):
        print('Inside disp3')
class Demo4(Demo3):
    pass
d4 = Demo4() # This is also not allowed because this class inherited from demo3 class which has abstract method...

'''
If abstract class can have only concrete method then object for that
abstract class can be created and concrete methods can be invoked...
'''