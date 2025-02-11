class Demo1:#Parent class
    def disp1(self):
        print("Inside disp1")
class Demo2(Demo1):#child class inheriting properties from parent class
    pass
d2 = Demo2() #Object creation 
d2.disp1()