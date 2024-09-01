import threading
import time





'''-----------------------------------------------------------------'''
# Define a function to be executed in a thread
def print_numbers():
    for i in range(5):
        print(f"Thread: {threading.current_thread().name}, Number: {i}")
        time.sleep(1)

# Create two thread objects
thread1 = threading.Thread(target=print_numbers, name='Thread 1')
thread2 = threading.Thread(target=print_numbers, name='Thread 2')

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Main thread exiting")
