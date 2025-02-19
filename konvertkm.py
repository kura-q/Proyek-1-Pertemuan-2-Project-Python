def konvertKm(angka) :
    pilihan = input("Konvert ke (HM, DAM, M, DM, CM, MM): ").upper()

    if pilihan == "HM" :
        angka = angka * 10
    elif pilihan == "DAM" :
        angka = angka * 100
    elif pilihan == "M" :
        angka = angka * 1000
    elif pilihan == "DM" :
        angka = angka * 10000
    elif pilihan == "CM" :
        angka = angka * 100000
    elif pilihan == "MM" :
        angka = angka * 1000000
    else :
        print("Pilihan tidak valid")
        return None
    
    return angka
