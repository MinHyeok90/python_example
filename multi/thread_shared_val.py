from threading import Thread
import time

start_time = time.time()

a = {}

class Val:
    def __init__(self):
        self.a = ""
        self.b = ""
        self.c = ""

    def __str__(self):
        return f"{self.a} {self.b} {self.c}"


def workb(val):
    for i in range(10):
        val.b = val.b + "B"
        val.c = val.c + "B"
        time.sleep(0.1)
        print(val.a)
    return


def worka(val):
    for i in range(10):
        val.a = val.a + "A"
        val.c = val.c + "A"
        time.sleep(0.1)
        print(val.b)
    return


if __name__ == "__main__":
    result = list()
    val = Val()
    th1 = Thread(target=worka, args=(val,))
    th2 = Thread(target=workb, args=(val,))
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()

print(f"Result: {val}") # Result: AAAAAAAAAA BBBBBBBBBB ABABBAABABBAABABBABA
print("--- %s seconds ---" % (time.time() - start_time)) # time 1 second
