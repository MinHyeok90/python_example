import multiprocessing
import time

start_time = time.time()

def count(name):
    for i in range(1, 100001):
        print(name, ' : ', i)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=4)
    pool.map(count, ['p1', 'p2', 'p3', 'p4'])
    pool.close()
    pool.join()

print("--- %s seconds ---" % (time.time() - start_time))