# Aurelia Clariza Hanani
# 065002500014

def dapatkan_akhiran_ordinal(n):
    if n == 0:
        return 'th'

    if 10 <= n % 100 <= 20:
        akhiran = 'th'
    else:
        digit_terakhir = n % 10

        if digit_terakhir == 1:
            akhiran = 'st'
        elif digit_terakhir == 2:
            akhiran = 'nd'
        elif digit_terakhir == 3:
            akhiran = 'rd'
        else:
            akhiran = 'th'

    return akhiran


print("Ordinal Number")
print("Ketik 0 untuk menghentikan program")

while True:
    angka = int(input("Masukkan angka: "))

    if angka == 0:
        print("Terima kasih telah menggunakan program saya.")
        break

    suffix = dapatkan_akhiran_ordinal(angka)

    print(f"({angka}, '{suffix}')")