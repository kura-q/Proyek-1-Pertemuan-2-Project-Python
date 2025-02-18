from konvertKM import * 
from konvertHM import *
from konvert_dam import *
from konvertM import *
from convert_dm import *
from konvertCm import *
from MMconversion import *
from fileHandling import *

pilih = input("Pilih mau konvert dari mana (KM, HM, DAM, M, DM, CM, MM)  : ").upper()
angka = float(input("input angka :"))

if pilih == "KM" :
    hasil = konvertKm(angka) #nama fungsi nya bebas 
elif pilih == "HM" :
    hasil = konvertHm(angka)
elif pilih == "DAM" :
    hasil = konvertDAM(angka)
elif pilih == "M" :
    hasil = konvertM(angka)
elif pilih == "DM" :
    hasil = convert_dm(angka)
elif pilih == "CM" :
    hasil = konvertCm(angka)
elif pilih == "MM" :
    hasil = conversion_MM(angka)

print(f"Hasil konversi: {hasil}")

simpan_riwayat_json(pilih, angka, hasil)

while True:
    print("\nMenu Riwayat:")
    print("1. Tampilkan Riwayat")
    print("2. Hapus Riwayat")
    print("3. Edit Riwayat")
    print("4. Keluar")
    pilihan_menu = int(input("Pilih menu: "))
    
    if pilihan_menu == 1:
        tampilkan_riwayat()
    elif pilihan_menu == 2:
        hapus_riwayat()
    elif pilihan_menu == 3:
        edit_riwayat()
    elif pilihan_menu == 4:
        break
    else:
        print("Pilihan tidak valid.")
