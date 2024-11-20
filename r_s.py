import threading
import time
class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.second = second
        self.minute = minute
    
    def update(self):
        self.second +=1
        if self.second == 60:
            self.second = 0
            self.minute +=1
            if self.minute == 60:
                self.minute = 0
                self.hour = (self.hour + 1)%24
    def __str__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


mutex = threading.Semaphore(1)
write_access = threading.Semaphore(1)
read_count = 0
clock = Clock(0,0,0)

def reader(id):
    global read_count
    while True:
        mutex.acquire()
        read_count += 1
        if read_count == 1:
            write_access.acquire()
        mutex.release()
        print(f"Reader {id} is reading the clock: {clock}")
        time.sleep(0.2)
        mutex.acquire()
        read_count -=1
        if read_count == 0:
            write_access.release()
        mutex.release()
        time.sleep(0.5)


def writer(id):
    while True:
        print(f"Writer {id} requesting access")
        write_access.acquire()
        print(f"Writer {id} Granted Access")
        clock.update()
        print(f"Writer {id} updated Clock {clock}")
        print(f"Writer {id} Releasing Access")
        write_access.release()
        import time
        time.sleep(1)

reader1 = threading.Thread(target=reader, args=(1,))
reader2 = threading.Thread(target=reader, args=(2,))
writer1 = threading.Thread(target=writer, args=(1,))
writer2 = threading.Thread(target=writer, args=(2,))

reader1.start()
reader2.start()
writer1.start()
writer2.start()