import threading
import time

def daemon():
    print("Job Started by {}".format(threading.current_thread().getName()))
    time.sleep(8)
    for i in range(1, 100):
        pass
    print("Job done by {}".format(threading.current_thread().getName()))

def nonDaemon():
    print("Job Started by {}".format(threading.current_thread().getName()))
    for i in range(1, 10000):
        for j in range(1,10000):
            k = i + j
    print("Job done by {}".format(threading.current_thread().getName()))

worker_1 = threading.Thread(target=daemon, name="Daemon Thread")
worker_2 = threading.Thread(target=nonDaemon, name="Non Daemon Thread")
worker_1.setDaemon(True)

worker_1.start()
worker_2.start()