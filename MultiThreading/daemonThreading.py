import threading
import time
def background_task():
     print(threading.current_thread())
     while True:
        print("Backgroundtask running...")
        time.sleep(1)
thread = threading.Thread(target=background_task,name='daemon')
thread.daemon = True
thread.start()

time.sleep(5)
print("Main Thread dead.")