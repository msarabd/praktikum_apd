print("MASUKKAN USERNAME (mahdi) DAN PASSWORD (067)")
user = (input("Masukkan username Anda = "))
pw = int(input("Masukkan password Anda = "))

if user == "mahdi" and pw == 67:
    print("LOGIN BERHASIL")
    print("\nSELAMAT DATANG TUAN MAHDI, HARI INI MAU KONVERSI APA??\n(panjang[1], massa[2], suhu[3], waktu[4], atau mata uang[5])")
    nilai = int(input("Masukkan kode konversi = "))

    if nilai == 1:
        print("\n|PILIHAN KONVERSI PANJANG|\n feet        >> meter    {1}\n kilometer   >> meter    {2}\n centimeter  >> meter    {3}")
        
        jenis = int(input("\nMasukkan kode konversi = "))
        if jenis == 1:
            konversi = float(input("Masukkan nilai (feet) = "))
            hasil = konversi * 0.3048
            print("Hasil konversi =", hasil, "meter")
        elif jenis == 2:
            konversi = float(input("Masukkan nilai (km) = "))
            hasil = konversi * 1000
            print("Hasil konversi =", hasil, "meter")
        elif jenis == 3:
            konversi = float(input("Masukkan nilai (cm) = "))
            hasil = konversi / 100
            print("Hasil konversi =", hasil, "meter")
        else:
            print("ERROR, MASUKKAN SESUAI KODE ANGKA YANG TELAH DIBERIKAN")

    elif nilai == 2:
        print("\n|PILIHAN KONVERSI MASSA|")
        print(" pound       >> kilogram {1}")
        print(" ton         >> kilogram {2}")
        print(" gram        >> kilogram {3}")
        print(" ons         >> kilogram {4}")
        print(" miligram    >> kilogram {5}")
        
        jenis = int(input("\nMasukkan kode = "))
        if jenis == 1:
            konversi = float(input("Masukkan nilai (pound) = "))
            hasil = konversi * 0.454
            print("Hasil konversi =", hasil, "kg")
        elif jenis == 2:
            konversi = float(input("Masukkan nilai (ton) = "))
            hasil = konversi * 1000
            print("Hasil konversi =", hasil, "kg")
        elif jenis == 3:
            konversi = float(input("Masukkan nilai (gram) = "))
            hasil = konversi / 1000
            print("Hasil konversi =", hasil, "kg")
        elif jenis == 4:
            konversi = float(input("Masukkan nilai (ons) = "))
            hasil = konversi / 10
            print("Hasil konversi =", hasil, "kg")
        elif jenis == 5:
            konversi = float(input("Masukkan nilai (mg) = "))
            hasil = konversi / 1000000
            print("Hasil konversi =", hasil, "kg")
        else:
            print("ERROR, MASUKKAN SESUAI KODE ANGKA YANG TELAH DIBERIKAN")

    elif nilai == 3:
        print("\n|PILIHAN KONVERSI SUHU|")
        print(" Celcius     >> Kelvin    {1}")
        print(" Fahrenheit  >> Kelvin    {2}")
        print(" Reamur      >> Kelvin    {3}")

        jenis = int(input("\nMasukkan kode konversi = "))
        if jenis == 1:
            konversi = float(input("Masukkan nilai ('C) = "))
            hasil = konversi + 273.15
            print("Hasil konversi =", hasil, "Kelvin")
        elif jenis == 2:
            konversi = float(input("Masukkan nilai ('F) = "))
            hasil = (konversi - 32) * 5/9 + 273.15
            print("Hasil konversi =", hasil, "Kelvin")
        elif jenis == 3:
            konversi = float(input("Masukkan nilai ('R) = "))
            hasil = konversi * 5/4 + 273.15
            print("Hasil konversi =", hasil, "Kelvin")
        else:
            print("ERROR, MASUKKAN SESUAI KODE ANGKA YANG TELAH DIBERIKAN")

    elif nilai == 4:
        print("\n|PILIHAN KONVERSI WAKTU|")
        print(" menit   >> detik    {1}")
        print(" jam     >> detik    {2}")
        
        jenis = int(input("\nMasukkan kode konversi = "))
        if jenis == 1:
            konversi = float(input("Masukkan nilai (m) = "))
            hasil = konversi * 60
            print("Hasil konversi =", hasil, "detik")
        elif jenis == 2:
            konversi = float(input("Masukkan nilai (h) = "))
            hasil = konversi * 3600
            print("Hasil konversi =", hasil, "detik")
        else:
            print("ERROR, MASUKKAN SESUAI KODE ANGKA YANG TELAH DIBERIKAN")

    elif nilai == 5:
        print("\n|PILIHAN KONVERSI MATA UANG|")
        print(" rupiah          >> dolar        {1}")
        print(" dolar           >> rupiah       {2}")
        print(" rupiah          >> yen          {3}")
        print(" yen             >> rupiah       {4}")
        print(" rupiah          >> dinar kuwait {5}")
        print(" dinar kuwait    >> rupiah       {6}")
        
        jenis = int(input("\nMasukkan kode konversi = "))
        if jenis == 1:
            konversi = float(input("Masukkan nilai (rupiah) = "))
            hasil = konversi / 16703
            print("Hasil konversi = $", hasil)
        elif jenis == 2:
            konversi = float(input("Masukkan nilai (dolar) = "))
            hasil = konversi * 16703
            print("Hasil konversi = Rp", hasil)
        elif jenis == 3:
            konversi = float(input("Masukkan nilai (rupiah) = "))
            hasil = konversi / 111.56
            print("Hasil konversi = Y", hasil)
        elif jenis == 4:
            konversi = float(input("Masukkan nilai (yen) = "))
            hasil = konversi * 111.56
            print("Hasil konversi = Rp", hasil)
        elif jenis == 5:
            konversi = float(input("Masukkan nilai (rupiah) = "))
            hasil = konversi / 54650.83
            print("Hasil konversi = D", hasil)
        elif jenis == 6:
            konversi = float(input("Masukkan nilai (dinar) = "))
            hasil = konversi * 54650.83
            print("Hasil konversi = Rp", hasil)
        else:
            print("ERROR, MASUKKAN SESUAI KODE ANGKA YANG TELAH DIBERIKAN")
    else:
            print("ERROR, MASUKKAN SESUAI KODE ANGKA YANG TELAH DIBERIKAN")

elif user == "mahdi" or pw == 67:
    if user == "mahdi":
        print("PASSWORD ANDA SALAH")
    else:
        print("USERNAME ANDA SALAH")
else:
    print("GAGAL LOGIN")