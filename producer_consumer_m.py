# producer_consumer_mutex.py
import threading
import time
import random
from threading import Lock, Condition
from collections import deque

# Shared variables
buffer = deque(maxlen=5)  # Fixed size buffer of 5
lock = Lock()
not_full = Condition(lock)
not_empty = Condition(lock)

def display_buffer():
    return f"Buffer: {list(buffer)} [Size: {len(buffer)}/5]"

def producer(id):
    count = 0
    while True:
        item = f"P{id}-{count}"
        
        with lock:
            while len(buffer) == 5:  # Buffer is full
                print(f"Producer {id} waiting - buffer full")
                not_full.wait()
            
            # Produce item
            buffer.append(item)
            print(f"Producer {id} produced {item}")
            print(display_buffer())
            
            not_empty.notify()  # Notify consumers
        
        count += 1
        time.sleep(random.uniform(0.5, 2))

def consumer(id):
    while True:
        with lock:
            while len(buffer) == 0:  # Buffer is empty
                print(f"Consumer {id} waiting - buffer empty")
                not_empty.wait()
            
            # Consume item
            item = buffer.popleft()
            print(f"Consumer {id} consumed {item}")
            print(display_buffer())
            
            not_full.notify()  # Notify producers
        
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    # Create producers and consumers
    producers = [threading.Thread(target=producer, args=(i,)) for i in range(2)]
    consumers = [threading.Thread(target=consumer, args=(i,)) for i in range(3)]
    
    # Start all threads
    for t in producers + consumers:
        t.daemon = True
        t.start()
    
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopping the program...")