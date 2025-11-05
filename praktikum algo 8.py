# Aurelia Clariza Hanani
# 065002500014

total = 0
jumlah = 0

while True:
    huruf = input("Masukkan Nilai: ").upper()

    if huruf== "":
        break

    if huruf == "A":
        nilai = 4.00
    elif huruf == "A-":
        nilai = 3.75
    elif huruf == "B+":
        nilai = 3.50
    elif huruf == "B":
        nilai = 3.00
    elif huruf == "B-":
        nilai = 2.75
    elif huruf == "C+":
        nilai = 2.50
    elif huruf == "C":
        nilai = 2.00
    elif huruf == "C-":
        nilai = 1.75
    elif huruf == "D":
        nilai = 1.50
    elif huruf == "E":
        nilai = 1.25
    else:
        print("Nilai huruf tidak valid")
        continue

    print(f"Nilai= {nilai}")
    total += nilai
    jumlah += 1

if jumlah > 0:
    rata = total / jumlah
    print(f"rata-ratanya adalah: {rata:.2f}")
else:
    print("Tidak ada nilai yang dimasukkan.")

