import tkinter as tk
from tkinter import messagebox
import math

def hitung_E1():
    try:
        f = float(entry_f.get())
        q = float(entry_q1.get())
        if q == 0:
            messagebox.showerror("Error", "Muatan (q) tidak boleh nol!")
            return
        hasil = f / q
        label_hasil1.config(text=f"E = {hasil:.2e} N/C")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

def hitung_E2():
    try:
        k = 9e9 
        q = float(entry_q2.get())
        r = float(entry_r.get())
        if r == 0:
            messagebox.showerror("Error", "Jarak (r) tidak boleh nol!")
            return
        hasil = k * (q / (r**2))
        label_hasil2.config(text=f"E = {hasil:.2e} N/C")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

def hitung_EC():
    try:
        ea = float(entry_ea.get())
        eb = float(entry_eb.get())
        sudut_deg = float(entry_angle.get())
        
        # Mengubah derajat ke radian karena math.cos menggunakan radian
        sudut_rad = math.radians(sudut_deg)
        
        # Rumus: EC = sqrt(EA^2 + EB^2 + 2*EA*EB*cos(alpha))
        persamaan = (ea**2) + (eb**2) + (2 * ea * eb * math.cos(sudut_rad))
        
        if persamaan < 0:
            messagebox.showerror("Error", "Hasil di bawah akar negatif. Periksa input sudut!")
            return
            
        ec = math.sqrt(persamaan)
        label_hasil_c.config(text=f"Ec = {ec:.2e} N/C")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# Setup Window Utama
root = tk.Tk()
root.title("Kalkulator Fisika: Medan Listrik")
root.geometry("450x700") # Ukuran sedikit lebih besar untuk menampung 3 bagian

# --- Bagian 1: E = F / q ---
frame1 = tk.LabelFrame(root, text="1. Rumus Dasar (E = F / q)", padx=10, pady=10)
frame1.pack(padx=10, pady=5, fill="x")

tk.Label(frame1, text="Gaya Coulomb (F) [N]:").grid(row=0, column=0, sticky="w")
entry_f = tk.Entry(frame1)
entry_f.grid(row=0, column=1)

tk.Label(frame1, text="Muatan Uji (q) [C]:").grid(row=1, column=0, sticky="w")
entry_q1 = tk.Entry(frame1)
entry_q1.grid(row=1, column=1)

btn_hitung1 = tk.Button(frame1, text="Hitung E", command=hitung_E1, bg="#fbbf24")
btn_hitung1.grid(row=2, columnspan=2, pady=5)

label_hasil1 = tk.Label(frame1, text="E = ...", font=("Arial", 10, "bold"))
label_hasil1.grid(row=3, columnspan=2)

# --- Bagian 2: E = k * q / r^2 ---
frame2 = tk.LabelFrame(root, text="2. Titik ke Muatan (E = k * q / r²)", padx=10, pady=10)
frame2.pack(padx=10, pady=5, fill="x")

tk.Label(frame2, text="Besar Muatan (q) [C]:").grid(row=0, column=0, sticky="w")
entry_q2 = tk.Entry(frame2)
entry_q2.grid(row=0, column=1)

tk.Label(frame2, text="Jarak (r) [m]:").grid(row=1, column=0, sticky="w")
entry_r = tk.Entry(frame2)
entry_r.grid(row=1, column=1)

btn_hitung2 = tk.Button(frame2, text="Hitung E", command=hitung_E2, bg="#fbbf24")
btn_hitung2.grid(row=2, columnspan=2, pady=5)

label_hasil2 = tk.Label(frame2, text="E = ...", font=("Arial", 10, "bold"))
label_hasil2.grid(row=3, columnspan=2)

# --- Bagian 3: Resultan Medan Listrik di Titik C ---
frame3 = tk.LabelFrame(root, text="3. Resultan Medan (Vektor) di Titik C", padx=10, pady=10, fg="blue")
frame3.pack(padx=10, pady=5, fill="x")

tk.Label(frame3, text="Medan EA [N/C]:").grid(row=0, column=0, sticky="w")
entry_ea = tk.Entry(frame3)
entry_ea.grid(row=0, column=1)

tk.Label(frame3, text="Medan EB [N/C]:").grid(row=1, column=0, sticky="w")
entry_eb = tk.Entry(frame3)
entry_eb.grid(row=1, column=1)

tk.Label(frame3, text="Sudut α (derajat):").grid(row=2, column=0, sticky="w")
entry_angle = tk.Entry(frame3)
entry_angle.grid(row=2, column=1)

btn_hitung_c = tk.Button(frame3, text="Hitung Ec", command=hitung_EC, bg="#60a5fa", fg="white")
btn_hitung_c.grid(row=3, columnspan=2, pady=5)

label_hasil_c = tk.Label(frame3, text="Ec = ...", font=("Arial", 10, "bold"))
label_hasil_c.grid(row=4, columnspan=2)

root.mainloop()