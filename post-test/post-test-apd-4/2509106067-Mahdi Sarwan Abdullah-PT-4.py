user = input("Masukkan username Anda = ").lower()
pw = input("Masukkan password Anda = ")

ulang = False
total_apos = 0
total_anet = 0
total_bpos = 0
total_bnet = 0
total_abpos = 0
total_abnet = 0
total_opos = 0
total_onet = 0
while ulang == False:
    while user != "mahdi" or pw != "067":
        if user == "" or pw == "":
            print("(Masukkan karakter)")
        elif user == "mahdi":
            print("(Hanya password yang salah)")
        elif pw == "067":
            print("(Hanya username yang salah)")
        else:
            print("(Username dan password Anda salah)")
        print("(Login kembali) \n")
        user = input("Masukkan username Anda = ")
        pw = input("Masukkan password Anda = ")

    gol_darah = input("\nGolongan darah Anda (A/B/AB/O) = ").upper()
    rhesus = input(f"Rhesus (+/-) = ")
    
    if gol_darah == "" or rhesus == "":
        print("(Masukkan karakter)")
        continue

    elif gol_darah == "A":
        if rhesus == "+":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("Masukkan jumlah kantong = "))
                if total_kantong == "":
                    print("(Masukkan karakter)\n")
                    continue
                elif not total_kantong.isdigit():
                    print("(Masukkan input berupa angka positif)\n")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("(Jumlah kantong darah harus lebih dari 0)\n")
                    continue                
                total_apos += total_kantong
                ulang2 = True
                
        elif rhesus == "-":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("Masukkan jumlah kantong = "))
                if total_kantong == "":
                    print("(Masukkan karakter)\n")
                    continue
                elif not total_kantong.isdigit():
                    print("(Masukkan input berupa angka positif)\n")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("(Jumlah kantong darah harus lebih dari 0)\n")
                    continue                
                total_anet += total_kantong
                ulang2 = True
        else:
            print("(Rhesus tidak sesuai)")
            continue
        
    elif gol_darah == "B":
        if rhesus == "+":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("Masukkan jumlah kantong = "))
                if total_kantong == "":
                    print("(Masukkan karakter)\n")
                    continue
                elif not total_kantong.isdigit():
                    print("(Masukkan input berupa angka positif)\n")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("(Jumlah kantong darah harus lebih dari 0)\n")
                    continue                
                total_bpos += total_kantong
                ulang2 = True
                
        elif rhesus == "-":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("Masukkan jumlah kantong = "))
                if total_kantong == "":
                    print("(Masukkan karakter)\n")
                    continue
                elif not total_kantong.isdigit():
                    print("(Masukkan input berupa angka positif)\n")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("(Jumlah kantong darah harus lebih dari 0)\n")
                    continue                
                total_bnet += total_kantong
                ulang2 = True
        else:
            print("(Rhesus tidak sesuai)")
            continue

    elif gol_darah == "AB":
        if rhesus == "+":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("Masukkan jumlah kantong = "))
                if total_kantong == "":
                    print("(Masukkan karakter)\n")
                    continue
                elif not total_kantong.isdigit():
                    print("(Masukkan input berupa angka positif)\n")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("(Jumlah kantong darah harus lebih dari 0)\n")
                    continue                
                total_abpos += total_kantong
                ulang2 = True

        elif rhesus == "-":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("Masukkan jumlah kantong = "))
                if total_kantong == "":
                    print("(Masukkan karakter)\n")
                    continue
                elif not total_kantong.isdigit():
                    print("(Masukkan input berupa angka positif)\n")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("(Jumlah kantong darah harus lebih dari 0)\n")
                    continue                
                total_abnet += total_kantong
                ulang2 = True
        else:
            print("(Rhesus tidak sesuai)")
            continue

    elif gol_darah == "O":
        if rhesus == "+":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("Masukkan jumlah kantong = "))
                if total_kantong == "":
                    print("(Masukkan karakter)\n")
                    continue
                elif not total_kantong.isdigit():
                    print("(Masukkan input berupa angka positif)\n")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("(Jumlah kantong darah harus lebih dari 0)\n")
                    continue                
                total_opos += total_kantong
                ulang2 = True
                
        elif rhesus == "-":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("Masukkan jumlah kantong = "))
                if total_kantong == "":
                    print("(Masukkan karakter)\n")
                    continue
                elif not total_kantong.isdigit():
                    print("(Masukkan input berupa angka positif)\n")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("(Jumlah kantong darah harus lebih dari 0)\n")
                    continue                
                total_onet += total_kantong
                ulang2 = True
        else:
            print("(Rhesus tidak sesuai)")
            continue

    else:
        print("(Golongan darah atau rhesus tidak sesuai)")
        continue

    ulang3 = False
    while ulang3 == False:
        terakhir = input("\nMau lanjut atau tidak (y/t)? ")
        if terakhir == "":
            print("(Masukkan karakter)")
            continue
        elif terakhir == "y":
            ulang3 = True
        elif terakhir == "t":
            ulang3 = True
            ulang = True
        else:
            print("(Input tidak valid)")

print("")
if total_apos > 0:
    kon_apos = total_apos * 500
    print("Jumlah darah A+ =", kon_apos, "ml")
if total_anet > 0:
    kon_anet = total_anet * 500
    print("Jumlah darah A- =", kon_anet, "ml")
if total_bpos > 0:
    kon_bpos = total_bpos * 500
    print("Jumlah darah B+ =", kon_bpos, "ml")
if total_bnet > 0:
    kon_bnet = total_bnet * 500
    print("Jumlah darah B- =", kon_bnet, "ml")
if total_abpos > 0:
    kon_abpos = total_abpos * 500
    print("Jumlah darah AB+ =", kon_abpos, "ml")
if total_abnet > 0:
    kon_abnet = total_abnet * 500
    print("Jumlah darah AB- =", kon_abnet, "ml")
if total_opos > 0:
    kon_opos = total_opos * 500
    print("Jumlah darah O+ =", kon_opos, "ml")
if total_onet > 0:
    kon_onet = total_onet * 500
    print("Jumlah darah O- =", kon_onet, "ml")
print("(selesai)")
