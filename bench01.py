import time
import timeit
import logging
from datetime import datetime

# setup logging for benchmarking
logging.basicConfig(filename="benchmark.log", level=logging.INFO)

def basic_timer():
    print("\nBasic time.time() benchmark")
    start = time.time()
    total = sum(range(1000000))
    end = time.time()
    print(f"Sum completed in {end - start:.6f} seconds")

def high_precision_timer():
    print("\nHigh-precision time.perf_counter() benchmark")
    start = time.perf_counter()
    total = sum(range(1000000))
    end = time.perf_counter()
    print(f"Sum completed in {end - start:.6f} seconds")

def timeit_benchmark():
    print("\n timeit module benchmark")
    duration = timeit.timeit("sum(range(1000000))", number=5)
    print(f"Average time over 5 runs: {duration / 5:.6f} seconds")

def log_benchmark():
    print("\n Logging benchmark with timestamp")
    start = datetime.now()
    total = sum(range(1000000))
    end = datetime.now()
    duration = (end - start).total_seconds()
    logging.info(f"Sum benchmark at {start} took {duration:.6f} seconds")
    print(f"Logging benchmark duration {duration:.6f} seconds")

def benchmark_playground():
    while True:
        print("\nChoose a benchmarking method:")
        print("1. Basic time.time()")
        print("2. High-precision time.perf_counter()")
        print("3. timeit module")
        print("4. Log benchmark with tinmestamp")
        print("5. quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            basic_timer()
        elif choice == "2":
            high_precision_timer()
        elif choice == "3":
            timeit_benchmark()
        elif choice == "4":
            log_benchmark()
        elif choice == "5":
            print("Exiting benchmark playground.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__=="__main__":
    benchmark_playground()
