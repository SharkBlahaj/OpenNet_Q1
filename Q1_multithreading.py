'''
### OpenNet - Python
Question 1: Multithreading

Problem Statement:
Write a Python program that simulates a producer-consumer scenario using multithreading. 
The producer thread should generate random integers and place them into a shared queue.
The consumer thread should read integers from the queue and print them. 
Use a threading lock to ensure thread-safe access to the queue.

Requirements:
- Use the threading module. 
- Implement a shared queue with a maximum size of 10.
- The producer should produce a new integer every 0.1 seconds. 
- The consumer should consume an integer every 0.15 seconds. 
- The program should run for 10 seconds before terminating.
'''

###########################################################################

import threading
import queue
import random
import time

def producer(q, lock, event):
    while not event.is_set():
        num = random.randint(1, 100)
        with lock:
            if not q.full():
                q.put(num)
                print(f"Produced: {num}, Queue size: {q.qsize()}")
        time.sleep(0.1)

def consumer(q, lock, event):
    while not event.is_set() or not q.empty():
        with lock:
            if not q.empty():
                num = q.get()
                print(f"Consumed: {num}, Queue size: {q.qsize()}")
        time.sleep(0.15)

def main():
    q = queue.Queue(maxsize=10)
    lock = threading.Lock()
    event = threading.Event()
    
    producer_thread = threading.Thread(target=producer, args=(q, lock, event))
    consumer_thread = threading.Thread(target=consumer, args=(q, lock, event))
    
    producer_thread.start()
    consumer_thread.start()
    
    start_time = time.time()
    time.sleep(10)
    event.set()

    producer_thread.join()
    consumer_thread.join()

    end_time = time.time()
    print(f"Program ran for {end_time - start_time} seconds.")
    print("Program terminated.")

if __name__ == "__main__":
    main()
