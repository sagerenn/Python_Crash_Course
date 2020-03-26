import threading
import os

def task1():
    print(f"Task 1 assigned to thread: {threading.current_thread().name}")
    print(f"ID of process running task 1: {os.getpid()}")

def task2():
    print(f"Task 2 assigned to thread: {threading.current_thread().name}")
    print(f"ID of process running task 1: {os.getpid()}")

if __name__ == '__main__':
    print(f"main thread name: {threading.current_thread().name}")
    print(f"main PID: {os.getpid()}")

    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()