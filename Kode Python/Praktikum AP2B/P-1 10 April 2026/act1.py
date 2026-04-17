import threading
import time

list_provinsi = [
    "Aceh",
    "Sumatera Utara",
    "Sumatera Barat",
    "Riau",
    "Jambi",
    "Sumatera Selatan",
    "Bangka Belitung",
    "DKI Jakarta",
    "DI Yogyakarta",
    "Jawa Timur",
    "Jawa Barat",
    "Jawa Tengah",
    "Bali",
    "Banten",
    "NTB",
    "NTT",
    "Kalimantan Barat",
    "Kalimantan Timur",
    "Kalimantan Selatan",
    "Sulawesi Tengah",
    "Sulawesi Barat",
    "Sulawesi Timur",
    "Sulawesi Selatan",
    "Sulawesi Tengah",
    "Gorontalo",
    "Maluku",
    "Papua", 
    "Papua Barat",
]

def print_provinsi(provinsi):
    time.sleep(1)
    with lock:
        print(f"Provinsi : {provinsi}")

start_time = time.time()
lock = threading.Lock()

threads = []
for provinsi in list_provinsi:
    thread = threading.Thread(target=print_provinsi, args=(provinsi,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

waktu_berlalu = time.time() - start_time

print (f"Waktu yang sudah berlalu : {waktu_berlalu:.2f} detik")