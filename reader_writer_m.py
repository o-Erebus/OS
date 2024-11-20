# reader_writer_mutex.py
import threading
import time
import random
from threading import Lock

class Clock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
    
    def update(self):
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes >= 60:
                self.minutes = 0
                self.hours = (self.hours + 1) % 24
    
    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

# Shared variables
read_lock = Lock()
write_lock = Lock()
reader_count = 0
clock = Clock()

def reader(reader_id):
    while True:
        global reader_count
        
        with read_lock:
            reader_count += 1
            print(f"Reader {reader_id}: Access granted")
            if reader_count == 1:
                write_lock.acquire()
                print(f"Reader {reader_id}: Blocking writers")

        # Reading the clock
        print(f"Reader {reader_id}: Current time is {clock}")
        time.sleep(random.uniform(0.2, 0.5))

        with read_lock:
            reader_count -= 1
            if reader_count == 0:
                write_lock.release()
                print(f"Reader {reader_id}: Allowing writers")
        time.sleep(0.1)

def writer(writer_id):
    while True:
        print(f"Writer {writer_id}: Requesting access")
        with write_lock:
            print(f"Writer {writer_id}: Access granted")
            
            # Updating clock
            clock.update()
            print(f"Writer {writer_id}: Updated time to {clock}")
            time.sleep(1)  # Wait 1 second before next update
            
        print(f"Writer {writer_id}: Released access")

if __name__ == "__main__":
    readers = [threading.Thread(target=reader, args=(i,)) for i in range(2)]
    writers = [threading.Thread(target=writer, args=(i,)) for i in range(2)]
    
    for t in readers + writers:
        t.daemon = True
        t.start()
    
    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopping the program...")