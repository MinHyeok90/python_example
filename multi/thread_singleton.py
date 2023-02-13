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
                    cls.a = "a"
                    cls.b = "b"
                    cls.c = "c"
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


# 이런 싱글톤 객체는 상속이 안된다. init이 호출되지 않기 때문.
# Child는 ThreadSafeSingleton일 뿐이며, 이 클래스 내에 추가된 함수는 초기화가 되지 않는다.
class Child(ThreadSafeSingleton):
    def __init__(self):
        self.a = "Child"
        print("Child")
    
    def printa(self):
        print(self.a)
        

c:Child = Child()
c.printa() # 이 함수는 존재하지 않는다. Child는 ThreadSafeSingleton일 뿐이다.

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
