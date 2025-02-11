class Demo:
    def disp(self):
        print('Inside disp with 0 parameter')
    def disp(self,a):
        print('Inside disp with 1 parameter')
    def disp(self,a,b):
        print('Inside disp with 2 parameter')
d = Demo()
d.disp()
d.disp(10)
d.disp(10,20)
