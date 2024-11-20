# producer_consumer_semaphore.py
import threading
import time
import random
from threading import Semaphore
from collections import deque

# Shared variables
buffer = deque(maxlen=5)  # Fixed size buffer of 5
empty = Semaphore(5)      # Initially 5 empty slots
full = Semaphore(0)       # Initially 0 full slots
mutex = Semaphore(1)      # Mutex for buffer access

def display_buffer():
    return f"Buffer: {list(buffer)} [Size: {len(buffer)}/5]"

def producer(id):
    count = 0
    while True:
        item = f"P{id}-{count}"
        
        empty.acquire()    # Wait if buffer is full
        mutex.acquire()    # Get exclusive access
        
        # Produce item
        buffer.append(item)
        print(f"Producer {id} produced {item}")
        print(display_buffer())
        
        mutex.release()    # Release exclusive access
        full.release()     # Signal one slot is full
        
        count += 1
        time.sleep(random.uniform(0.5, 2))

def consumer(id):
    while True:
        full.acquire()     # Wait if buffer is empty
        mutex.acquire()    # Get exclusive access
        
        # Consume item
        item = buffer.popleft()
        print(f"Consumer {id} consumed {item}")
        print(display_buffer())
        
        mutex.release()    # Release exclusive access
        empty.release()    # Signal one slot is empty
        
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