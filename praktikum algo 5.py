# Aurelia Clariza Hanani
# 065002500014

nama = input("Masukkan Nama: ")
nim = input("Masukkan Nim: ")
total = int(input("Masukkan Total Belanja: Rp "))
kupon = input("Masukkan Kode Kupon: ")

if kupon == "IKL639":
    print("SELAMAT ANDA MENDAPATKAN DISKON 100%")
    diskon = 1.0
    potongan = total
    bayar = 0
else:
    if 40000 <= total <= 89999:
        diskon = 0.2
    elif 90000 <= total <= 189999:
        diskon = 0.4
    elif 190000 <= total <= 389999:
        diskon = 0.6
    elif total >= 390000:
        diskon = 0.8
    else:
        diskon = 0.0

    potongan = total * diskon
    bayar = total - potongan

print(f"Total Belanja : Rp {total}")
print(f"Diskon : {int(diskon*100)}%")
print(f"Potongan : Rp {int(potongan)}")
print(f"Total Bayar : Rp {int(bayar)}")

print("Terimakasih sudah belanja")