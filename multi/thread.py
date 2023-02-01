from threading import Thread
import time

start_time = time.time()

a = "+"

def workb():
    global a
    for i in range(10):
        a = a + "2"
        time.sleep(0.1)
    return


def worka():
    global a
    for i in range(10):
        a = a + str("1")
        time.sleep(0.1)
    return

def work(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.append(total)
    return

if __name__ == "__main__":
    START, END = 0, 100000000
    result = list()
    th1 = Thread(target=worka, args=())
    th2 = Thread(target=workb, args=())
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()

print(f"Result: {a}")
print("--- %s seconds ---" % (time.time() - start_time))
