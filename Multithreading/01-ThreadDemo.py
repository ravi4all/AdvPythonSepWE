import threading

def job_1():
    print("Job Started by Thread_1")
    for i in range(1,10000):
        for j in range(1,1010):
            i+j
    print("Job done by Thread_1")

def job_2():
    print("Job Started by Thread_2")
    for i in range(1,100):
        pass
    print("Job done by Thread_2")

# print(threading.current_thread().getName())
# job_1()
# job_2()

worker_1 = threading.Thread(target=job_1, name="Worker_1")
worker_2 = threading.Thread(target=job_2, name="Worker_2")

worker_1.start()
worker_2.start()