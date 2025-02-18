def konvertCm(angka) :
    pilihan = input("Konvert ke (KM, DAM, M, DM, CM, MM): ").upper()

    if pilihan == "KM" :
        angka = angka // 10
    elif pilihan == "DAM" :
        angka = angka * 10
    elif pilihan == "M" :
        angka = angka * 100
    elif pilihan == "DM" :
        angka = angka * 1000
    elif pilihan == "CM" :
        angka = angka * 10000
    elif pilihan == "MM" :
        angka = angka * 100000
    else :
        print("Pilihan tidak valid")
        return None
    
    return angka
