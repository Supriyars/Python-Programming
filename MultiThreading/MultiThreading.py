import threading 
import time
print(threading.current_thread())
li1 = [1,2,3,4,5]
li2 = ['a','b','c','d','e']

def displayDigits(li1):
    for i in li1:
        print(i)
        time.sleep(2)
def displayLetters(li2):
    for i in li2:
        print(i)
        time.sleep(1)
t1 = threading.Thread(target=displayDigits,args=(li1,))
t2 = threading.Thread(target=displayLetters,args=(li2,))
t1.start()
t2.start()