import json

# Fungsi untuk menyimpan riwayat ke file JSON
def simpan_riwayat_json(pilih, angka, hasil):
    data = {
        "unit": pilih,
        "angka_awal": angka,
        "hasil_konversi": hasil
    }
    
    try:
        with open("riwayat_konversi.json", "r") as file:
            riwayat = json.load(file)
    except FileNotFoundError:
        riwayat = []

    riwayat.append(data)  # Menambah riwayat konversi ke list

    with open("riwayat_konversi.json", "w") as file:
        json.dump(riwayat, file, indent=4)
    
    print("Riwayat konversi telah disimpan ke JSON.")

# Fungsi untuk menampilkan riwayat konversi
def tampilkan_riwayat():
    try:
        with open("riwayat_konversi.json", "r") as file:
            riwayat = json.load(file)
            for index, item in enumerate(riwayat, 1):
                print(f"{index}. {item['unit']} | {item['angka_awal']} -> {item['hasil_konversi']}")
    except FileNotFoundError:
        print("Riwayat tidak ditemukan.")

# Fungsi untuk menghapus riwayat berdasarkan nomor
def hapus_riwayat():
    tampilkan_riwayat()  # Tampilkan riwayat yang ada
    try:
        riwayat = json.load(open("riwayat_konversi.json", "r"))
        index_hapus = int(input("Masukkan nomor riwayat yang ingin dihapus: ")) - 1
        
        if 0 <= index_hapus < len(riwayat):
            del riwayat[index_hapus]  # Hapus riwayat berdasarkan index
            with open("riwayat_konversi.json", "w") as file:
                json.dump(riwayat, file, indent=4)
            print("Riwayat telah dihapus.")
        else:
            print("Nomor riwayat tidak valid.")
    except FileNotFoundError:
        print("Tidak ada riwayat untuk dihapus.")

# Fungsi untuk mengedit riwayat berdasarkan nomor
def edit_riwayat():
    tampilkan_riwayat()  # Tampilkan riwayat yang ada
    try:
        riwayat = json.load(open("riwayat_konversi.json", "r"))
        index_edit = int(input("Masukkan nomor riwayat yang ingin diedit: ")) - 1

        if 0 <= index_edit < len(riwayat):
            unit_baru = input("Masukkan unit baru (KM, HM, DAM, M, DM, CM, MM): ").upper()
            angka_baru = float(input("Masukkan angka baru: "))
            hasil_baru = float(input("Masukkan hasil konversi baru: "))

            riwayat[index_edit] = {
                "unit": unit_baru,
                "angka_awal": angka_baru,
                "hasil_konversi": hasil_baru
            }

            with open("riwayat_konversi.json", "w") as file:
                json.dump(riwayat, file, indent=4)

            print("Riwayat telah diperbarui.")
        else:
            print("Nomor riwayat tidak valid.")
    except FileNotFoundError:
        print("Tidak ada riwayat untuk diedit.")
