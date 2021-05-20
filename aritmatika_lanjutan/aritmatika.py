def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    return a / b


def hasilBagi(a, b):
    return a % b


def pangkat(a, b):
    return a ** b


def tampil():
    print("--- MENU ---")
    print(
        "1. Tambah\n2. Kurang\n3. Kali\n4. Bagi\n5. Hasil Bagi\n6. Pangkat\n0. Exit"
    )
    pil = int(input("Masukkan pilihan : "))
    proses(pil)

def proses(pil):
    int(pil)
    if pil == 1:
        print("Fungsi Tambah")
        a = int(input("Angka ke -1 = "))
        b = int(input("Angka ke -2 = "))
        print("Penjumlahan dari a dan b adalah", tambah(a, b))
    elif pil == 2:
        print("Fungsi Kurang")
        a = int(input("Angka ke -1 = "))
        b = int(input("Angka ke -2 = "))
        print("Pengurangan dari a dan b adalah", kurang(a, b))
    elif pil == 3:
        print("Fungsi Kali")
        a = int(input("Angka ke -1 = "))
        b = int(input("Angka ke -2 = "))
        print("Perkalian dari a dan b adalah", kali(a, b))
    elif pil == 4:
        print("Fungsi Bagi")
        a = int(input("Angka ke -1 = "))
        b = int(input("Angka ke -2 = "))
        print("Pembagian dari a dan b adalah", bagi(a, b))
    elif pil == 5:
        print("Fungsi Hasil Bagi")
        a = int(input("Angka ke -1 = "))
        b = int(input("Angka ke -2 = "))
        print("Hasil Bagi dari a dan b adalah", hasilBagi(a, b))
    elif pil == 6:
        print("Fungsi Pangkat")
        a = int(input("Angka ke -1 = "))
        b = int(input("Angka ke -2 = "))
        print("Perpangkatan dari a dan b adalah", pangkat(a, b))
    elif pil == 0:
        return 0
    else:
        return tampil()
