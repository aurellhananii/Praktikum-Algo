# Aurelia Clariza Hanani
# 065002500014

def konversi(huruf='A'):
    if huruf == 'A':
        return 4
    elif huruf == 'B':
        return 3
    elif huruf == 'C':
        return 2
    elif huruf == 'D':
        return 1
    else:
        return 0

total = 0
jumlah = 0

while True:
    huruf = input("masukkan nilai: ").upper()
    if huruf == "":
        break
    nilai = konversi(huruf)
    if nilai is not None:
        print("nilai =", nilai)
        total += nilai
        jumlah += 1
    else:
        print("Nilai tidak valid, masukkan A-E saja!")
if jumlah > 0:
    rata = total / jumlah
    print("Rata-ratanya adalah:", rata)
else:
    print("Tidak ada nilai yang dimasukkan.")