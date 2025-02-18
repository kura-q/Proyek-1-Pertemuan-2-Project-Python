def simpan_riwayat_text(pilih, angka, hasil):
    data = f"{pilih} | {angka} -> {hasil}\n"
    
    try:
        with open("history.txt", "a") as file: 
            file.write(data)  
        print("Riwayat konversi telah disimpan.")
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan riwayat: {e}")

def tampilkan_riwayat():
    try:
        with open("history.txt", "r") as file:
            riwayat = file.readlines()
            if riwayat:
                for index, item in enumerate(riwayat, 1):
                    print(f"{index}. {item.strip()}")
            else:
                print("Riwayat kosong.")
    except FileNotFoundError:
        print("Riwayat tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def hapus_riwayat():
    tampilkan_riwayat()  
    try:
        with open("history.txt", "r") as file:
            riwayat = file.readlines()
        
        index_hapus = int(input("Masukkan nomor riwayat yang ingin dihapus: ")) - 1
        
        if 0 <= index_hapus < len(riwayat):
            riwayat.pop(index_hapus)  
            
            with open("history.txt", "w") as file:
                file.writelines(riwayat)
            print("Riwayat telah dihapus.")
        else:
            print("Nomor riwayat tidak valid.")
    except FileNotFoundError:
        print("Tidak ada riwayat untuk dihapus.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def edit_riwayat():
    tampilkan_riwayat()  
    try:
        with open("history.txt", "r") as file:
            riwayat = file.readlines()

        index_edit = int(input("Masukkan nomor riwayat yang ingin diedit: ")) - 1

        if 0 <= index_edit < len(riwayat):
            unit_baru = input("Masukkan unit baru (KM, HM, DAM, M, DM, CM, MM): ").upper()
            angka_baru = float(input("Masukkan angka baru: "))
            hasil_baru = float(input("Masukkan hasil konversi baru: "))

            riwayat[index_edit] = f"{unit_baru} | {angka_baru} -> {hasil_baru}\n"
            
            with open("history.txt", "w") as file:
                file.writelines(riwayat)

            print("Riwayat telah diperbarui.")
        else:
            print("Nomor riwayat tidak valid.")
    except FileNotFoundError:
        print("Tidak ada riwayat untuk diedit.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
