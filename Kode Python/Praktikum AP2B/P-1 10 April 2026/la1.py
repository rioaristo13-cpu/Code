import threading
import time

class DataProcessor:
    def __init__ (self):
        self.lock = threading.Lock()
        self.counter = 0
    
    def process_data_dengan_lock(self):
        with self.lock:
            sementara = self.counter
            time.sleep(0.000000001)
            sementara += 1
            self.counter = sementara

    def process_data_tanpa_lock(self):
        sementara = self.counter
        time.sleep(0.000000001)
        sementara += 1
        self.counter = sementara

def run_thread_dengan_lock(data_processor):
    for i in range(100000):
        data_processor.process_data_dengan_lock()

def run_thread_tanpa_lock(data_processor):
    for i in range(100000):
        data_processor.process_data_tanpa_lock()

#Dengan Lock
data_processor1 = DataProcessor()

thread1 = threading.Thread(target=run_thread_dengan_lock, args=(data_processor1,))
thread2 = threading.Thread(target=run_thread_dengan_lock, args=(data_processor1,))

print("Memulai perhitungan dengan 2 Thread ... (Dengan Lock)")

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f"Target Counter Seharusnya         : 200000")
print(f"Hasil Akhir Counter (Dengan Lock) : {data_processor1.counter}")

#Tanpa Lock
data_processor2 = DataProcessor()

thread3 = threading.Thread(target=run_thread_tanpa_lock, args=(data_processor2,))
thread4 = threading.Thread(target=run_thread_tanpa_lock, args=(data_processor2,))

print("\nMemulai perhitungan dengan 2 Thread ... (Tanpa Lock)")

thread3.start()
thread4.start()

thread3.join()
thread4.join()

print(f"Target Counter Seharusnya        : 200000")
print(f"Hasil Akhir Counter (Tanpa Lock) : {data_processor2.counter}")