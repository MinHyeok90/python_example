from multiprocessing import Process, Queue
import time
start_time = time.time()

def work2(id, start, end, result):
    total = 0
    for i in range(start, end):
        total += i
    result.put(total)
    return


def work(id, start, end, result):
    
    th1 = Process(target=work2, args=(3, start, end//2, result))
    th2 = Process(target=work2, args=(4, end//2, end, result))
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()

    
if __name__ == "__main__":
    START, END = 0, 100000000
    result = Queue()
    th1 = Process(target=work, args=(1, START, END//2, result))
    th2 = Process(target=work, args=(2, END//2, END, result))
    
    th1.start()
    th2.start()
    th1.join()
    th2.join()

    result.put('STOP')
    total = 0
    while True:
        tmp = result.get()
        if tmp == 'STOP':
            break
        else:
            total += tmp
    print(f"Result: {total}")
    print("--- %s seconds ---" % (time.time() - start_time))
