nilai = int(input("Masukkan angka = "))
if nilai > 80 and nilai <= 100:
    if nilai > 85:
        print("A+")
    else:
        print("A--")

elif nilai > 70 and nilai <= 80:
    if nilai > 75:
        print("B+")
    else:
        print("B")

elif nilai > 60 and nilai <= 70:
    if nilai > 65:
        print("C+")
    else:
        print("C")

else:
    print("D")

