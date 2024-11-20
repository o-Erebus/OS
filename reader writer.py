import threading
import time

# Shared custom clock
class CustomClock:
    def __init__(self):
        self.hours = 0
        self.minutes = 0
        self.seconds = 0

    def update(self):
        """Updates the clock by one second."""
        self.seconds += 1
        if self.seconds >= 60:
            self.seconds = 0
            self.minutes += 1
        if self.minutes >= 60:
            self.minutes = 0
            self.hours += 1
        if self.hours >= 24:
            self.hours = 0

    def get_time(self):
        """Returns the current time as a formatted string."""
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# Shared resources
custom_clock = CustomClock()
custom_clock.hours = 23
custom_clock.minutes = 59
custom_clock.seconds = 55
read_count = 0  # Number of active readers

# Synchronization primitives
mutex = threading.Lock()  # For updating read_count
rw_lock = threading.Semaphore(1)  # For exclusive writer access
 
def writer(writer_id):
    while True:
        print(f"Writer {writer_id} is waiting to access the clock...")
        rw_lock.acquire()  # Writer gains exclusive access
        print(f"Writer {writer_id} is updating the clock...")
        custom_clock.update()
        print(f"Writer {writer_id} updated clock to: {custom_clock.get_time()}")
        rw_lock.release()  # Writer releases access
        time.sleep(2)  # Simulate time before next write

def reader(reader_id):
    global read_count
    while True:
        print(f"Reader {reader_id} is waiting to read the clock...")
        with mutex:
            read_count += 1
            if read_count == 1:
                rw_lock.acquire()  # First reader locks writers
        print(f"Reader {reader_id} is reading the clock: {custom_clock.get_time()}")
        time.sleep(1)  # Simulate reading delay
        with mutex:
            read_count -= 1
            if read_count == 0:
                rw_lock.release()  # Last reader releases writers
        time.sleep(2)  # Simulate time before next read

# Create threads
writers = [threading.Thread(target=writer, args=(i,)) for i in range(1, 2)]
readers = [threading.Thread(target=reader, args=(i,)) for i in range(1, 3)]

# Start threads
for thread in writers + readers:
    thread.start()

# Join threads
for thread in writers + readers:
    thread.join()
