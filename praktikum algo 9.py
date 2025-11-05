# Aurelia Clariza Hanani
# 065002500014

total = 0.0

while True:
    umur = input("Masukkan umur: ")

    if umur == "":
        break
    umur = int(umur)

    if umur <= 2:
        harga = 0
        print("Gratis")
    elif 3 <= umur <= 12:
        harga = 14
        print("Harga $14.00")
    elif umur >= 65:
        harga = 18
        print("Harga $18.00")
    else:
        harga = 23
        print("Harga $23.00")

    total += harga
    print(f"Running total: {total:.2f}")

uang = float(input("Masukkan jumlah uang: "))
kembalian = uang - total
print(f"Running kembalian: {kembalian:.2f}")