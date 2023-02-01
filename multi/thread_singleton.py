import threading
import time

start_time = time.time()

a = {}
class ThreadSafeSingleton(object):
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if not cls._instance:  # This is the only difference
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
                    cls.a = ""
                    cls.b = ""
                    cls.c = ""
        return cls._instance

    def getA(self):
        return self.a
    
    def getB(self):
        return self.b
    
    def getC(self):
        return self.c

    def setA(self, a):
        self.a = a

    def setB(self, b):
        self.b = b

    def setC(self, c):
        self.c = c

    def __str__(self):
        return f"{self.a} {self.b} {self.c}"


def workb():
    val:ThreadSafeSingleton = ThreadSafeSingleton()
    for i in range(10):
        val.setB(val.getB() + "B")
        val.setC(val.getC() + "B")
        print(val.b)
    return


def worka():
    val = ThreadSafeSingleton()
    for i in range(10):
        val.setA(val.getA() + "A")
        val.setC(val.getC() + "A")
        print(val.a)
    return


if __name__ == "__main__":
    result = list()
    th1 = threading.Thread(target=worka, args=())
    th2 = threading.Thread(target=workb, args=())
    
    th1.start()
    th2.start()
    th1.join() # join은 해당 thread가 끝날때까지 기다린다. 해당 thread가 끝나지 않으면 다음 코드를 실행하지 않는다.
    th2.join()
    print("done")

val = ThreadSafeSingleton()
print(f"Result: {val}") # Result: AAAAAAAAAA BBBBBBBBBB ABABBAABABBAABABBABA
print("--- %s seconds ---" % (time.time() - start_time)) # time 1 second
