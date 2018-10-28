import threading
import time

def job_1():
    print("Job Started by {}".format(threading.current_thread().getName()))
    time.sleep(4)
    for i in range(1, 100):
        pass
    print("Job done by {}".format(threading.current_thread().getName()))

def job_2():
    print("Job Started by {}".format(threading.current_thread().getName()))
    for i in range(1, 100):
        for j in range(1,10000):
            k = i + j
    print("Job done by {}".format(threading.current_thread().getName()))

worker_1 = threading.Thread(target=job_1, name="Worker_1")
worker_2 = threading.Thread(target=job_2, name="Worker_2")

worker_1.start()
worker_2.start()