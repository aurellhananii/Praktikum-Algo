# Aurelia Clariza Hanani
# 065002500014

def is_kabisat(tahun):

    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

def hitung_hari(bulan, tahun):
    
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    
    elif bulan in [4, 6, 9, 11]:
        return 30
    
    elif bulan == 2:
        if is_kabisat(tahun):
            return 29  
        else:
            return 28  
            
    else:
        return None

print("Masukkan 0 untuk menghentikan program\n")
    
while True:
    bulan = int(input("Masukkan bulan (1-12): "))
            
    if bulan == 0:
        print("Program dihentikkan.")
        break
    tahun = int(input("\nmasukkan tahun (e.g., 2021): "))
    hari = hitung_hari(bulan, tahun)

    if hari:
         print(f"{hari} hari dalam sebulan\n")
    else:
        print("Input bulan tidak valid\n")
            