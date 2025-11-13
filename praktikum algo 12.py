# Aurelia Clariza Hanani
# 065002500014

def cek_prima(x):
    if x <= 1:
        return False
    elif x == 2:
        return True
    for i in range(2, x):
        if x % i == 0:
             return False  
        return True

def tampil_hasil_prima(angka, status):
    if status:
        print(f"{angka} adalah bilangan Prima")
    else:
        print(f"{angka} bukanlah bilangan Prima")

while True:
    angka_input = int(input("Masukkan Angka (0 untuk berhenti): "))
    if angka_input == 0:
        print("Program selesai.")
        break

    status = cek_prima(angka_input)
    tampil_hasil_prima(angka_input, status)  