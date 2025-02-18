def konvertDAM(angka) :
    pilihan = input("Konvert ke (KM, HM, M, DM, CM, MM): ").upper()

    if pilihan == "KM" :
        angka = angka // 100
    elif pilihan == "HM" :
        angka = angka // 10
    elif pilihan == "M" :
        angka = angka * 10
    elif pilihan == "DM" :
        angka = angka * 100
    elif pilihan == "CM" :
        angka = angka * 1000
    elif pilihan == "MM" :
        angka = angka * 10000
    else :
        print("Pilihan tidak valid")
        return None
    
    return angka