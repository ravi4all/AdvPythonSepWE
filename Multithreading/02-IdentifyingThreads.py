import threading

def job():
    print("Job Started by {}".format(threading.current_thread().getName()))
    for i in range(1,10000):
        for j in range(1,1010):
            i+j
    print("Job done by {}".format(threading.current_thread().getName()))

# print(threading.current_thread().getName())
# job_1()
# job_2()

# worker_1 = threading.Thread(target=job, name="Worker_1")
# worker_2 = threading.Thread(target=job, name="Worker_2")
#
# worker_1.start()
# worker_2.start()

for i in range(10):
    worker = threading.Thread(target=job, name="Worker_{}".format(i))
    worker.start()