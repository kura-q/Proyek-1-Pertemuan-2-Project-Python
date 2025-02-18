def convert_dm(x) :
    ke = input("ke : ").lower()

    if ke == "km" :
        hasil = x//10000
    elif ke == "hm" :
        hasil = x//1000
    elif ke == "dam" : 
        hasil = x//100
    elif ke == "m" :
        hasil = x//10
    elif ke == "cm" :
        hasil = x*10
    elif ke == "mm" :
        hasil = x*100
    else :
        print("Pilihan tidak valid")
        return None
    
    return hasil