user = input("Masukkan username Anda = ").lower()
pw = input("Masukkan password Anda = ")

ulang = False
ulang3 = False
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
            print("Masukkan karakter")
        elif user == "mahdi":
            print("Password Anda salah")
        elif pw == "067":
            print("Username Anda salah")
        else:
            print("Username dan password Anda salah")
        print("Login kembali \n")
        user = input("Masukkan username Anda = ")
        pw = input("Masukkan password Anda = ")

    gol_darah = input("\nGolongan darah Anda (A/B/AB/O) = ").upper()
    rhesus = input(f"Rhesus (+/-) = ")
    
    if gol_darah == "" or rhesus == "":
        print("Masukkan karakter")
        continue

    elif gol_darah == "A":
        if rhesus == "+":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("\nMasukkan jumlah kantong = "))
                if total_kantong == "":
                    print("Masukkan karakter")
                    continue
                elif not total_kantong.isdigit():
                    print("Masukkan input berupa angka positif")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("Jumlah kantong darah harus lebih dari 0")
                    continue                
                total_apos += total_kantong
                kon_apos = total_apos * 500
                print("Total jumlah darah A+ =", kon_apos, "ml")
                ulang2 = True
                
        elif rhesus == "-":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("\nMasukkan jumlah kantong = "))
                if total_kantong == "":
                    print("Masukkan karakter")
                    continue
                elif not total_kantong.isdigit():
                    print("Masukkan input berupa angka positif")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("Jumlah kantong darah harus lebih dari 0")
                    continue                
                total_anet += total_kantong
                kon_anet = total_anet * 500
                print("Total jumlah darah A- =", kon_anet, "ml")
                ulang2 = True

    elif gol_darah == "B":
        if rhesus == "+":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("\nMasukkan jumlah kantong = "))
                if total_kantong == "":
                    print("Masukkan karakter")
                    continue
                elif not total_kantong.isdigit():
                    print("Masukkan input berupa angka positif")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("Jumlah kantong darah harus lebih dari 0")
                    continue                
                total_bpos += total_kantong
                kon_bpos = total_bpos * 500
                print("Total jumlah darah B+ =", kon_bpos, "ml")
                ulang2 = True

                
        elif rhesus == "-":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("\nMasukkan jumlah kantong = "))
                if total_kantong == "":
                    print("Masukkan karakter")
                    continue
                elif not total_kantong.isdigit():
                    print("Masukkan input berupa angka positif")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("Jumlah kantong darah harus lebih dari 0")
                    continue                
                total_bnet += total_kantong
                kon_bnet = total_bnet * 500
                print("Total jumlah darah B- =", kon_bnet, "ml")
                ulang2 = True
    
    elif gol_darah == "AB":
        if rhesus == "+":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("\nMasukkan jumlah kantong = "))
                if total_kantong == "":
                    print("Masukkan karakter")
                    continue
                elif not total_kantong.isdigit():
                    print("Masukkan input berupa angka positif")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("Jumlah kantong darah harus lebih dari 0")
                    continue                
                total_abpos += total_kantong
                kon_abpos = total_abpos * 500
                print("Total jumlah darah AB+ =", kon_abpos, "ml")
                ulang2 = True

        elif rhesus == "-":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("\nMasukkan jumlah kantong = "))
                if total_kantong == "":
                    print("Masukkan karakter")
                    continue
                elif not total_kantong.isdigit():
                    print("Masukkan input berupa angka positif")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("Jumlah kantong darah harus lebih dari 0")
                    continue                
                total_abnet += total_kantong
                kon_abnet = total_abnet * 500
                print("Total jumlah darah AB- =", kon_abnet, "ml")
                ulang2 = True

    elif gol_darah == "O":
        if rhesus == "+":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("\nMasukkan jumlah kantong = "))
                if total_kantong == "":
                    print("Masukkan karakter")
                    continue
                elif not total_kantong.isdigit():
                    print("Masukkan input berupa angka positif")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("Jumlah kantong darah harus lebih dari 0")
                    continue                
                total_opos += total_kantong
                kon_opos = total_opos * 500
                print("Total jumlah darah O+ =", kon_opos, "ml")
                ulang2 = True
                
        elif rhesus == "-":
            ulang2 = False
            while ulang2 == False:
                total_kantong = (input("\nMasukkan jumlah kantong = "))
                if total_kantong == "":
                    print("Masukkan karakter")
                    continue
                elif not total_kantong.isdigit():
                    print("Masukkan input berupa angka positif")
                    continue
                total_kantong = int(total_kantong)
                if total_kantong == 0:
                    print("Jumlah kantong darah harus lebih dari 0")
                    continue                
                total_onet += total_kantong
                kon_onet = total_onet * 500
                print("Total jumlah darah O- =", kon_onet, "ml")
                ulang2 = True
    else:
        print("Golongan darah atau rhesus tidak sesuai")
        continue

    while ulang3 == False:
        terakhir = input("\nMau lanjut atau tidak (y/t)? ")
        if terakhir == "":
            print("Masukkan karakter")
            continue
        elif terakhir == "y":
            ulang3 = True
        elif terakhir == "t":
            ulang3 = True
        else:
            print("Input tidak valid")

    ulang = True
        
if total_apos >= 0:
    print("Total darah A+ = ", kon_apos)
if total_anet >= 0:
    print("Total darah A- = ", kon_anet)
if total_bpos >= 0:
    print("Total darah B+ = ", kon_bpos)
if total_bnet >= 0:
    print("Total darah B- = ", kon_bnet)
if total_abpos >= 0:
    print("Total darah AB+ = ", kon_abpos)
if total_abnet >= 0:
    print("Total darah A+ = ", kon_abnet)
if total_opos >= 0:
    print("Total darah A+ = ", kon_opos)
if total_onet >= 0:
    print("Total darah A+ = ", kon_onet)
print("selesai")
