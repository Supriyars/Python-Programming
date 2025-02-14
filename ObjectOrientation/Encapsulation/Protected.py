class Demo1:#Base class
    def __init__(self,name):
        self._firstname =name # -_firstname -> protected variable
    def disp1(self):
        print(self._firstname) 
d1 = Demo1('Akash')
print(d1._firstname)
d1.disp1()
class Demo2(Demo1): #Child class
    def disp2(self):
        print(self._firstname)
d2 = Demo2('Pooja')
print(d2._firstname)
d2.disp2()
class Demo3:
    def disp3(self):
        print(d1._firstname)
d3 = Demo3()
d3.disp3()

'''
1...The variables which are protected ,can be accessed inside the same class 
,outside of any class, inside the child class,inside the non child class..
2...The variables which are protected, should be accessed inside the same class
and inside the child class and this is programmers duty to follow these rules...
'''

