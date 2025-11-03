from multiprocessing import Process
import os
import time


def square_numbers_worker(num):
    for i in range(num + 1):
        result = i * i
        print('Sleeping to simulate work...')
        time.sleep(0.1)  # Simulate a time-consuming task
    print(f"Process ID: {os.getpid()} - The square of {num} is {result}")


processes = []
for i in range(os.cpu_count()):
    process = Process(target=square_numbers_worker, args=(i + 1,))
    processes.append(process)
    process.start()

for process in processes:
    process.join()  # Wait for the process to finish before starting the next one

print("All processes have completed.")
