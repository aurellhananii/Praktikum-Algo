# Aurelia Clariza Hanani
# 065002500014

import os

def buat_file():
    nama_file = input("Masukkan Nama File (contoh: Biodata2): ")
    nama_file = nama_file + ".txt"

    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    angkatan = input("Masukkan Angkatan: ")

    with open(nama_file, "w") as f:
        f.write(f"Nama: {nama}\n")
        f.write(f"NIM: {nim}\n")
        f.write(f"Angkatan: {angkatan}\n")

    print("\nFile Berhasil Dibuat dan Ditulis!\n")

def baca_file():
    nama_file = input("Masukkan Nama File: ") + ".txt"

    if not os.path.exists(nama_file):
        print("File tidak ditemukan!\n")
        return

    print("\nIsi File:")
    with open(nama_file, "r") as f:
        print(f.read())

def tambah_text():
    nama_file = input("Masukkan Nama File: ") + ".txt"

    if not os.path.exists(nama_file):
        print("File tidak ditemukan!\n")
        return

    sahabat = input("Masukkan Nama Sahabatmu: ")
    catatan = input("Masukkan Catatan Tambahan kamu: ")

    with open(nama_file, "a") as f:
        f.write(f"Nama Sahabat: {sahabat}\n")
        f.write(f"Catatan: {catatan}\n")

    print("\nData Berhasil Ditambahkan\n")

while True:
    print("===== Program File Handling =====")
    print("1. Membuat dan Menulis File")
    print("2. Membaca File")
    print("3. Menambahkan Text Pada File")
    print("4. Keluar Dari Program")

    pilihan = input("\nMasukkan Pilihan Berupa Angka (1/2/3/4): ")

    if pilihan == "1":
        buat_file()

    elif pilihan == "2":
        baca_file()

    elif pilihan == "3":
        tambah_text()

    elif pilihan == "4":
        print("Terima Kasih Sudah Menggunakan Program Saya")
        break

    else:
        print("Pilihan tidak valid!\n")