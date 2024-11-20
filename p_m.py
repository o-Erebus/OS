import threading
from collections import deque
import time
buffer = deque(maxlen=5)
mutex = threading.Lock()
not_full = threading.Condition(mutex)
not_empty = threading.Condition(mutex)
count = 0
def Producer(id):
    global count
    while True:
        mutex.acquire()
        while len(buffer) == 5:
            not_full.wait()
        
        count +=1
        print(f"Producer {id} Produced {count}")
        buffer.append(count)
        print(buffer)
        
        not_empty.notify()
        mutex.release()
        time.sleep(1)

def Consumer(id):
    global count
    while True:
        mutex.acquire()
        while len(buffer) == 0:
            not_empty.wait()
        
        print(f"Consumer {id} Consumed {buffer.popleft()}")
        print(f"{buffer}")
        not_full.notify()
        mutex.release()
        time.sleep(1)

p1 = threading.Thread(target=Producer,args=(1,))

p2 = threading.Thread(target=Producer,args=(2,))
p3 = threading.Thread(target=Producer,args=(3,))
c1 = threading.Thread(target=Consumer,args=(1,))
c2 = threading.Thread(target=Consumer,args=(2,))

p1.start()
p2.start()
p3.start()
c1.start()
c2.start()