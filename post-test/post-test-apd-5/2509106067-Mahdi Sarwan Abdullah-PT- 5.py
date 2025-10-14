import os
os.system("cls")
data_admin = [["mahdi", "067"]]
data_pengguna = [["arya", "068"]]
login_admin = False
login_user = False

gk_utama = ["Marten Paes"]
df_utama = ["Jay Idzes",
            "Rizky Ridho",
            "Justin Hubner", 
            "Calvin Verdonk", 
            "Kevin Diks",
            ]
mf_utama = ["Thom Haye", 
            "Joel Pelupessy", 
            "Marselino",
            ]
fw_utama = ["Rafael Struick", 
            "Ole Romeny",
            ]

gk_cadangan = ["Emil Audero",
               "Nadeo Argawinata",
               ]
df_cadangan = ["Mees Hilgers",
               "Sandy Walsh",
               "Yakob Sayuri",
               "Yance Sayuri",
               "Justin Hubner",
               ]
mf_cadangan = ["Ivar Jenner",
               "Ricky Kambuaya",
               ]
fw_cadangan = ["Ragnar Oratmangoen",
               "Miliano Jonathans",
               "Egy Maulana Vikry",
               ]

awal_1 = False
while awal_1 == False:
    print("""ANDA INGIN LOGIN SEBAGAI:
    1. Pengguna Biasa
    2. Sebagai Admin 
    3. Daftar Sebagai Pengguna Baru""")
    pilihan_1 = input("Pilih menu (1-3) = ").strip()

    while True:
        os.system("cls")
        if pilihan_1 == "":
            print("""ANDA INGIN LOGIN SEBAGAI:
    1. Pengguna Biasa
    2. Sebagai Admin 
    3. Daftar Sebagai Pengguna Baru""")
            print("(Masukkan karakter)")
            pilihan_1 = input("Pilih menu (1-3) = ").strip()
            continue
        elif not pilihan_1.isdigit() or pilihan_1 == "0":
            print("""ANDA INGIN LOGIN SEBAGAI:
    1. Pengguna Biasa
    2. Sebagai Admin 
    3. Daftar Sebagai Pengguna Baru""")
            print("(Input Anda tidak valid)")
            pilihan_1 = input("Pilih menu (1-3) = ").strip()
            continue
        break

    if pilihan_1 == "1":
        os.system("cls")
        ulang1 = False
        while ulang1 == False:
            print("=== Login Sebagai User Biasa ===\n")
            user = input("Masukkan username Anda = ").strip().lower()
            pw = input("Masukkan password Anda = ").strip().lower()

            while user == "" or pw == "":
                os.system("cls")
                print("(Masukkan karakter)\n")
                print("=== Login Sebagai User Biasa ===\n")
                user = input("Masukkan username Anda = ").strip().lower()
                pw = input("Masukkan password Anda = ").strip().lower()

            for pengguna in data_pengguna:
                os.system("cls")
                if user == pengguna[0] and pw == pengguna[1]:
                    print("Login berhasil")
                    login_user = True
                    ulang1 = True
                    awal_1 = True
                    break
                elif user == pengguna[0] or pw == pengguna[1]:
                    if user == pengguna[0]:
                        print("Hanya password yang salah")
                        break
                    else:
                        print("Hanya username yang salah")
                        break
            
    elif pilihan_1 == "2":
        os.system("cls")
        print("=== Login Sebagai Admin ===\n")
        user = input("Masukkan username Anda = ").strip().lower()
        pw = input("Masukkan password Anda = ").strip().lower()

        while user != data_admin[0][0] or pw != data_admin[0][1]:
            if user == "" or pw == "":
                input("(Masukkan karakter, tekan enter untuk kembali)")
            elif user == data_admin[0][0]:
                input("(Hanya password yang salah, tekan enter untuk kembali)")
            elif pw == data_admin[0][1]:
                input("(Hanya username yang salah, tekan enter untuk kembali)")
            else:
                input("(Username dan password Anda salah, tekan enter untuk kembali)")
            os.system("cls")
            print("=== Login Sebagai Admin ===\n")
            user = input("Masukkan username Anda = ").strip().lower()
            pw = input("Masukkan password Anda = ").strip().lower()

        os.system("cls")
        login_admin = True
        awal_1 = True

    elif pilihan_1 == "3":
        os.system("cls")
        print("=== Menu Register ===\n")
        user = input("Masukkan username Anda = ").strip().lower()
        pw = input("Masukkan password Anda = ").strip().lower()

        while True:
            os.system("cls")
            if user == "" or pw == "":
                print("(Masukkan karakter)\n")
            elif not pw.isdigit():
                print("(Masukkan input berupa angka positif)\n")
            else:
                break
            print("(Login kembali) \n")
            user = input("Masukkan username Anda = ").strip().lower()
            pw = input("Masukkan password Anda = ").strip().lower()

        data_pengguna.append([user, pw])
        print("(Login berhasil, login ulang)\n")


if login_admin:
    while login_admin:
        os.system("cls")
        print("=== Selamat Datang Tuan Muda Mahdi ===\n")
        print("""Mau ngapain hari ini?
[1] Lihat Daftar Line Up
[2] Tambah Pemain Cadangan
[3] Ganti Starting Line Up
[4] Ganti Pemain Cadangan
[5] Hapus Pemain Cadangan
[6] Keluar""")
        pilihan_2 = input("Pilih menu (1-6) = ").strip()
        
        if pilihan_2 == "1":
            os.system("cls")
            print("Daftar Line Up Timnas Indonesia {10-14-25}\n")
            print("Starting:")
            for i in range(len(gk_utama)):
                print(f"    {i+1}. {gk_utama[i]} (GK)")
            for i in range(len(df_utama)):
                print(f"    {i+2}. {df_utama[i]} (DF)")
            for i in range(len(mf_utama)):
                print(f"    {i+7}. {mf_utama[i]} (MF)")
            for i in range(len(fw_utama)):
                print(f"    {i+10}. {fw_utama[i]} (FW)")
            
            print("\nCadangan:")
            for i in range(len(gk_cadangan)):
                print(f"    {i+1}. {gk_cadangan[i]} (GK)")
            for i in range(len(df_cadangan)):
                print(f"    {i+1+len(gk_cadangan)}. {df_cadangan[i]} (DF)")
            for i in range(len(mf_cadangan)):
                print(f"    {i+1+len(gk_cadangan + df_cadangan)}. {mf_cadangan[i]} (MF)")
            for i in range(len(fw_cadangan)):
                print(f"    {i+1+len(gk_cadangan + df_cadangan + mf_cadangan)}. {fw_cadangan[i]} (FW)")
            input("\n(Ketuk enter untuk kembali memilih menu)")
        
        elif pilihan_2 == "2":
            os.system("cls")
            print("Cadangan:")
            for i in range(len(gk_cadangan)):
                print(f"    {i+1}. {gk_cadangan[i]} (GK)")
            for i in range(len(df_cadangan)):
                print(f"    {i+1+len(gk_cadangan)}. {df_cadangan[i]} (DF)")
            for i in range(len(mf_cadangan)):
                print(f"    {i+1+len(gk_cadangan + df_cadangan)}. {mf_cadangan[i]} (MF)")
            for i in range(len(fw_cadangan)):
                print(f"    {i+1+len(gk_cadangan + df_cadangan + mf_cadangan)}. {fw_cadangan[i]} (FW)")
            pemain_tambahan = input("\nMasukkan nama pemain = ").strip()
            pilihan_3 = input("Pilih lini yang ingin diganti (GK/DF/MF/FW) = ").strip().upper()
            while True:
                if pilihan_3 == "GK":
                    gk_cadangan.append(pemain_tambahan)
                    break
                elif pilihan_3 == "DF":
                    df_cadangan.append(pemain_tambahan)
                    break
                elif pilihan_3 == "MF":
                    mf_cadangan.append(pemain_tambahan)
                    break
                elif pilihan_3 == "FW":
                    fw_cadangan.append(pemain_tambahan)
                    break
                else:
                    input("\n(Input tidak valid, tekan enter untuk kembali)")
                os.system("cls")
                print("Cadangan:")
                for i in range(len(gk_cadangan)):
                    print(f"    {i+1}. {gk_cadangan[i]} (GK)")
                for i in range(len(df_cadangan)):
                    print(f"    {i+1+len(gk_cadangan)}. {df_cadangan[i]} (DF)")
                for i in range(len(mf_cadangan)):
                    print(f"    {i+1+len(gk_cadangan + df_cadangan)}. {mf_cadangan[i]} (MF)")
                for i in range(len(fw_cadangan)):
                    print(f"    {i+1+len(gk_cadangan + df_cadangan + mf_cadangan)}. {fw_cadangan[i]} (FW)")
                pemain_tambahan = input("\nMasukkan nama pemain = ").strip()
                pilihan_3 = input("Pilih lini yang ingin diganti (GK/DF/MF/FW) = ").strip().upper()
            
            print(f"(Sukses menambahkan {pemain_tambahan} ke dalam lini {pilihan_3})")
            input("\n(Ketuk enter untuk kembali memilih menu)")

        elif pilihan_2 == "4":
            os.system("cls")
            print("Cadangan:")
            for i in range(len(gk_cadangan)):
                print(f"    {i+1}. {gk_cadangan[i]} (GK)")
            for i in range(len(df_cadangan)):
                print(f"    {i+2}. {df_cadangan[i]} (DF)")
            for i in range(len(mf_cadangan)):
                print(f"    {i+7}. {mf_cadangan[i]} (MF)")
            for i in range(len(fw_cadangan)):
                print(f"    {i+10}. {fw_cadangan[i]} (FW)")
            
            pemain_tukar = input("\nMasukkan nama pemain = ").strip()
            pilihan_3 = input("Pilih lini yang ingin diganti (GK/DF/MF/FW) = ").strip().upper()
            print("")
            while True:
                if pilihan_3 == "GK":
                    for i in range(len(gk_cadangan)):
                        print(f"    {i+1}. {gk_cadangan[i]} (GK)")
                    pemain_diganti = int(input("\nMasukkan angka pemain yang ingin diganti = ").strip()) - 1
                    gk_cadangan[pemain_diganti] = pemain_tukar
                    break
                elif pilihan_3 == "DF":
                    for i in range(len(df_cadangan)):
                        print(f"    {i+1}. {df_cadangan[i]} (DF)")
                    pemain_diganti = int(input("\nMasukkan angka pemain yang ingin diganti = ").strip()) - 1
                    df_cadangan[pemain_diganti] = pemain_tukar
                    break
                elif pilihan_3 == "MF":
                    for i in range(len(mf_cadangan)):
                        print(f"    {i+1}. {mf_cadangan[i]} (MF)")
                    pemain_diganti = int(input("\nMasukkan angka pemain yang ingin diganti = ").strip()) - 1
                    mf_cadangan[pemain_diganti] = pemain_tukar
                    break
                elif pilihan_3 == "FW":
                    for i in range(len(fw_cadangan)):
                        print(f"    {i+1}. {fw_cadangan[i]} (FW)")
                    pemain_diganti = int(input("\nMasukkan angka pemain yang ingin diganti = ").strip()) - 1
                    fw_cadangan[pemain_diganti] = pemain_tukar
                    break
                else:
                    input("\n(Input tidak valid, tekan enter untuk kembali)")
                os.system("cls")
                print("Cadangan:")
                for i in range(len(gk_cadangan)):
                    print(f"    {i+1}. {gk_cadangan[i]} (GK)")
                for i in range(len(df_cadangan)):
                    print(f"    {i+1+len(gk_cadangan)}. {df_cadangan[i]} (DF)")
                for i in range(len(mf_cadangan)):
                    print(f"    {i+1+len(gk_cadangan + df_cadangan)}. {mf_cadangan[i]} (MF)")
                for i in range(len(fw_cadangan)):
                    print(f"    {i+1+len(gk_cadangan + df_cadangan + mf_cadangan)}. {fw_cadangan[i]} (FW)")
                pemain_tukar = input("\nMasukkan nama pemain = ").strip()
                pilihan_3 = input("Pilih lini yang ingin diganti (GK/DF/MF/FW) = ").strip().upper()
                print("")
        
            print(f"(Sukses mengganti pemain dengan {pemain_tukar})")
            input("\n(Ketuk enter untuk kembali memilih menu)")
        
        elif pilihan_2 == "3":
            os.system("cls")
            print("Starting:")
            for i in range(len(gk_utama)):
                print(f"    {i+1}. {gk_utama[i]} (GK)")
            for i in range(len(df_utama)):
                print(f"    {i+2}. {df_utama[i]} (DF)")
            for i in range(len(mf_utama)):
                print(f"    {i+7}. {mf_utama[i]} (MF)")
            for i in range(len(fw_utama)):
                print(f"    {i+10}. {fw_utama[i]} (FW)")
            
            pemain_tukar = input("\nMasukkan nama pemain = ").strip()
            pilihan_3 = input("Pilih lini yang ingin diganti (GK/DF/MF/FW) = ").strip().upper()
            print("")
            while True:
                if pilihan_3 == "GK":
                    for i in range(len(gk_utama)):
                        print(f"    {i+1}. {gk_utama[i]} (GK)")
                    pemain_diganti = int(input("\nMasukkan angka pemain yang ingin diganti = ").strip()) - 1
                    gk_utama[pemain_diganti] = pemain_tukar
                    break
                elif pilihan_3 == "DF":
                    for i in range(len(df_utama)):
                        print(f"    {i+1}. {df_utama[i]} (DF)")
                    pemain_diganti = int(input("\nMasukkan angka pemain yang ingin diganti = ").strip()) - 1
                    df_utama[pemain_diganti] = pemain_tukar
                    break
                elif pilihan_3 == "MF":
                    for i in range(len(mf_utama)):
                        print(f"    {i+1}. {mf_utama[i]} (MF)")
                    pemain_diganti = int(input("\nMasukkan angka pemain yang ingin diganti = ").strip()) - 1
                    mf_utama[pemain_diganti] = pemain_tukar
                    break
                elif pilihan_3 == "FW":
                    for i in range(len(fw_utama)):
                        print(f"    {i+1}. {fw_utama[i]} (FW)")
                    pemain_diganti = int(input("\nMasukkan angka pemain yang ingin diganti = ").strip()) - 1
                    fw_utama[pemain_diganti] = pemain_tukar
                    break
                else:
                    input("\n(Input tidak valid, tekan enter untuk kembali)")
                os.system("cls")
                print("utama:")
                for i in range(len(gk_utama)):
                    print(f"    {i+1}. {gk_utama[i]} (GK)")
                for i in range(len(df_utama)):
                    print(f"    {i+1+len(gk_utama)}. {df_utama[i]} (DF)")
                for i in range(len(mf_utama)):
                    print(f"    {i+1+len(gk_utama + df_utama)}. {mf_utama[i]} (MF)")
                for i in range(len(fw_utama)):
                    print(f"    {i+1+len(gk_utama + df_utama + mf_utama)}. {fw_utama[i]} (FW)")
                pemain_tukar = input("\nMasukkan nama pemain = ").strip()
                pilihan_3 = input("Pilih lini yang ingin diganti (GK/DF/MF/FW) = ").strip().upper()
                print("")
        
            print(f"(Sukses mengganti pemain dengan {pemain_tukar})")
            input("\n(Ketuk enter untuk kembali memilih menu)")
        
        elif pilihan_2 == "5":
            os.system("cls")
            print("Cadangan:")
            for i in range(len(gk_cadangan)):
                print(f"    {i+1}. {gk_cadangan[i]} (GK)")
            for i in range(len(df_cadangan)):
                print(f"    {i+2}. {df_cadangan[i]} (DF)")
            for i in range(len(mf_cadangan)):
                print(f"    {i+7}. {mf_cadangan[i]} (MF)")
            for i in range(len(fw_cadangan)):
                print(f"    {i+10}. {fw_cadangan[i]} (FW)")
            
            pilihan_3 = input("\nPilih lini yang ingin dihapus (GK/DF/MF/FW) = ").strip().upper()
            print("")
            while True:
                if pilihan_3 == "GK":
                    for i in range(len(gk_cadangan)):
                        print(f"    {i+1}. {gk_cadangan[i]} (GK)")
                    pemain_dihapus = int(input("\nMasukkan angka pemain yang ingin dihapus = ").strip()) - 1
                    panggil_pemain = gk_cadangan[pemain_dihapus]
                    del gk_cadangan[pemain_dihapus]
                    break
                elif pilihan_3 == "DF":
                    for i in range(len(df_cadangan)):
                        print(f"    {i+1}. {df_cadangan[i]} (DF)")
                    pemain_dihapus = int(input("\nMasukkan angka pemain yang ingin dihapus = ").strip()) - 1
                    panggil_pemain = df_cadangan[pemain_dihapus]
                    del df_cadangan[pemain_dihapus]
                    break
                elif pilihan_3 == "MF":
                    for i in range(len(mf_cadangan)):
                        print(f"    {i+1}. {mf_cadangan[i]} (MF)")
                    pemain_dihapus = int(input("\nMasukkan angka pemain yang ingin dihapus = ").strip()) - 1
                    panggil_pemain = mf_cadangan[pemain_dihapus]
                    del mf_cadangan[pemain_dihapus]
                    break
                elif pilihan_3 == "FW":
                    for i in range(len(fw_cadangan)):
                        print(f"    {i+1}. {fw_cadangan[i]} (FW)")
                    pemain_dihapus = int(input("\nMasukkan angka pemain yang ingin dihapus = ").strip()) - 1
                    panggil_pemain = fw_cadangan[pemain_dihapus]
                    del fw_cadangan[pemain_dihapus]
                    break
                else:
                    input("\n(Input tidak valid, tekan enter untuk kembali)")
                os.system("cls")
                print("Cadangan:")
                for i in range(len(gk_cadangan)):
                    print(f"    {i+1}. {gk_cadangan[i]} (GK)")
                for i in range(len(df_cadangan)):
                    print(f"    {i+1+len(gk_cadangan)}. {df_cadangan[i]} (DF)")
                for i in range(len(mf_cadangan)):
                    print(f"    {i+1+len(gk_cadangan + df_cadangan)}. {mf_cadangan[i]} (MF)")
                for i in range(len(fw_cadangan)):
                    print(f"    {i+1+len(gk_cadangan + df_cadangan + mf_cadangan)}. {fw_cadangan[i]} (FW)")
                
                pilihan_3 = input("\nPilih lini yang ingin dihapus (GK/DF/MF/FW) = ").strip().upper()
                print("")
        
            print(f"(Sukses menghapus {panggil_pemain})")
            input("\n(Ketuk enter untuk kembali memilih menu)")
        
        elif pilihan_2 == "6":
            login_admin = False

        else:
            input("\n(Input tidak valid, tekan enter untuk kembali)")

if login_user:
    while login_user:
        os.system("cls")
        print(f"=== Selamat Datang Tuan Muda {user} ===\n")
        print("""Mau ngapain hari ini?
[1] Lihat Daftar Line Up
[2] Keluar""")
        pilihan_2 = input("Pilih menu (1-2) = ").strip()
        
        if pilihan_2 == "1":
            os.system("cls")
            print("Daftar Line Up Timnas Indonesia {10-14-25}\n")
            print("Starting:")
            for i in range(len(gk_utama)):
                print(f"    {i+1}. {gk_utama[i]} (GK)")
            for i in range(len(df_utama)):
                print(f"    {i+2}. {df_utama[i]} (DF)")
            for i in range(len(mf_utama)):
                print(f"    {i+7}. {mf_utama[i]} (MF)")
            for i in range(len(fw_utama)):
                print(f"    {i+10}. {fw_utama[i]} (FW)")

            print("\nCadangan:")
            for i in range(len(gk_cadangan)):
                print(f"    {i+1}. {gk_cadangan[i]} (GK)")
            for i in range(len(df_cadangan)):
                print(f"    {i+1+len(gk_cadangan)}. {df_cadangan[i]} (DF)")
            for i in range(len(mf_cadangan)):
                print(f"    {i+1+len(gk_cadangan + df_cadangan)}. {mf_cadangan[i]} (MF)")
            for i in range(len(fw_cadangan)):
                print(f"    {i+1+len(gk_cadangan + df_cadangan + mf_cadangan)}. {fw_cadangan[i]} (FW)")
            input("\n(Ketuk enter untuk kembali memilih menu)")

        elif pilihan_2 == "2":
            login_user = False

        else:
            input("\n(Input tidak valid, tekan enter untuk kembali)")

os.system("cls")
print(f"✨ Terima kasih atas waktunya, {user}. Sampai jumpa di lain kesempatan! Selamat tinggal. 👋")