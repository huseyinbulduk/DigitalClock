import tkinter as tk
import time

# Saat güncelleme fonksiyonu
def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_time)

# Ana pencere oluşturma
root = tk.Tk()
root.title("Dijital Saat")

# Saat etiketi oluşturma
clock_label = tk.Label(root, font=('Arial', 48), bg='black', fg='white')
clock_label.pack(pady=20)

# Saati güncelleme fonksiyonunu çağırma
update_time()

# Pencereyi çalıştırma
root.mainloop()
