import threading
import time
from collections import deque

buffer = deque(maxlen=5)
empty = threading.Semaphore(5)
full = threading.Semaphore(0)
mutex = threading.Semaphore(1)
count = 0
def Producer(id):
    global count
    while True:
        empty.acquire()
        mutex.acquire()

        count+=1
        buffer.append(count)
        print(f"Producer {id} Produced {count}")
        print(buffer)

        mutex.release()
        full.release()
        time.sleep(1)

def Consumer(id):
    global count
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer.popleft()
        print(f"Consumer {id} consumed {item}")
        print(buffer)
        empty.release()
        mutex.release()
        time.sleep(1)

p1 = threading.Thread(target=Producer,args=(1,))

p2 = threading.Thread(target=Producer,args=(2,))

c1 = threading.Thread(target=Consumer,args=(1,))
c2 = threading.Thread(target=Consumer,args=(2,))

p1.start()
p2.start()
p3.start()
c1.start()
c2.start()