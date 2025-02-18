def mm_ke_cm(a) :
    return a / 10

def mm_ke_dm(a) :
    return a / 100

def mm_ke_m(a) :
    return a / 1000

def mm_ke_dam(a) :
    return a / 10000

def mm_ke_hm(a) :
    return a / 100000

def mm_ke_km(a) :
    return a / 1000000

def conversion_MM(angka) :
    tujuan = input("Konvert ke (KM, HM, DAM, M, DM, CM): ").upper()
    if tujuan == "KM" :
        angka = mm_ke_km(angka)
    elif tujuan == "HM" :
        angka = mm_ke_hm(angka)
    elif tujuan == "DAM" :
        angka = mm_ke_dam(angka)
    elif tujuan == "M" :
        angka = mm_ke_m(angka)
    elif tujuan == "DM" :
        angka = mm_ke_dm(angka)
    elif tujuan == "CM" :
        angka = mm_ke_cm(angka)
    else :
        print("Pilihan tidak valid")
        return None
    
    return angka