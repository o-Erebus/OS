import threading
import time

class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    def update(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour = (self.hour+1)%24
    def __str__(self) -> str:
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


clock = Clock(0,0,0)
read_lock = threading.Lock()
write_lock = threading.Lock()
read_count = 0

def Reader(id):
    global read_count
    while True:
        read_lock.acquire()
        read_count += 1
        if read_count == 1:
            write_lock.acquire()
        read_lock.release()
        print(f"Reader {id} : {clock}")
        time.sleep(0.2)

        read_lock.acquire()
        read_count -= 1
        if read_count == 0:
            write_lock.release()
        read_lock.release()
        time.sleep(0.1)
        

def Writer(id):
    while True:
        write_lock.acquire()
        clock.update()
        print(f"Writer {id}: Updated Clock {clock}")
        write_lock.release()
        time.sleep(1)


reader1 = threading.Thread(target=Reader,args=(1,))
reader2 = threading.Thread(target=Reader,args=(2,))
writer1 = threading.Thread(target=Writer,args=(1,))
writer2 = threading.Thread(target=Writer,args=(2,))

reader1.start()

writer1.start()
writer2.start()
reader2.start()