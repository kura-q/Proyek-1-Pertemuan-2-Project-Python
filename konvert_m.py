def konvertM(angka) :
    pilihan = input("Konvert ke (KM, HM, DAM, DM, CM, MM): ").upper()

    if pilihan == "KM" :
        angka = angka // 1000
    elif pilihan == "HM" :
        angka = angka // 100
    elif pilihan == "DAM" :
        angka = angka // 10
    elif pilihan == "DM" :
        angka = angka * 10
    elif pilihan == "CM" :
        angka = angka * 100
    elif pilihan == "MM" :
        angka = angka * 1000
    else :
        print("Pilihan tidak valid")
        return None
    
    return angka