import os
os.system("cls")

data_pengguna = {
    "user_admin" : ["admin"],
    "pw_admin" : ["admin123"],
    "user_biasa" : ["arya"],
    "pw_biasa" : ["068"]
}

login_admin = False
login_user = False

data_pemain = {
    "gk_utama" : ["Marten Paes"],
    "df_utama" : ["Jay Idzes",
                  "Rizky Ridho",
                  "Justin Hubner", 
                  "Calvin Verdonk", 
                  "Kevin Diks"
                  ],
    "mf_utama" : ["Thom Haye",
                  "Joel Pelupessy", 
                  "Marselino"
                  ],
    "fw_utama" : ["Rafael Struick",
                  "Ole Romeny"
                  ],
    "gk_cadangan" : ["Emil Audero",
                     "Nadeo Argawinata"
                     ],
    "df_cadangan" : ["Mees Hilgers",
                     "Sandy Walsh",
                     "Yakob Sayuri",
                     "Yance Sayuri",
                     "Justin Hubner"
                     ],
    "mf_cadangan" : ["Ivar Jenner",
                     "Ricky Kambuaya"
                     ],
    "fw_cadangan" : ["Ragnar Oratmangoen",
                     "Miliano Jonathans",
                     "Egy Maulana Vikry"
                     ],
}
semua_pemain = data_pemain["gk_utama"] + data_pemain["df_utama"] + data_pemain["mf_utama"] + data_pemain["fw_utama"] + data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"] + data_pemain["fw_cadangan"]
cek_pemain = set(semua_pemain)

awal_1 = False
while awal_1 == False:
    os.system("cls")
    print("""ANDA INGIN LOGIN SEBAGAI:
    1. Pengguna Biasa
    2. Sebagai Admin 
    3. Daftar Sebagai Pengguna Baru""")
    pilihan_1 = input("Pilih menu (1-3) = ").strip()
    while True:
        if pilihan_1 == "":
            input("\n(Masukkan karakter, ketuk enter untuk memilih kembali)")
            os.system("cls")
            print("""ANDA INGIN LOGIN SEBAGAI:
    1. Pengguna Biasa
    2. Sebagai Admin 
    3. Daftar Sebagai Pengguna Baru""")
            pilihan_1 = input("Pilih menu (1-3) = ").strip()
            continue
        elif not pilihan_1.isdigit() or pilihan_1 == "0":
            input("\n(Masukkan angka sesuai pilihan, ketuk enter untuk memilih kembali)")
            os.system("cls")
            print("""ANDA INGIN LOGIN SEBAGAI:
    1. Pengguna Biasa
    2. Sebagai Admin 
    3. Daftar Sebagai Pengguna Baru""")
            pilihan_1 = input("Pilih menu (1-3) = ").strip()
            continue
        break

    if pilihan_1 == "1":
        ulang1 = False
        while ulang1 == False:
            awal_1 = False
            os.system("cls")
            print("=== Login Sebagai User Biasa ===\n")
            user = input("Masukkan username Anda = ").strip()
            pw = input("Masukkan password Anda = ").strip()

            while user == "" or pw == "":
                input("\n(Masukkan karakter, tekan enter untuk login kembali)")
                os.system("cls")
                print("=== Login Sebagai User Biasa ===\n")
                user = input("Masukkan username Anda = ").strip()
                pw = input("Masukkan password Anda = ").strip()

            for i in range(len(data_pengguna["user_biasa"])):
                if user == data_pengguna["user_biasa"][i] and pw == data_pengguna["pw_biasa"][i]:
                    input("\n(Login berhasil, ketuk enter untuk lanjut)")
                    login_user = True
                    ulang1 = True
                    awal_1 = True
                    break
                elif user == data_pengguna["user_biasa"][i] or pw == data_pengguna["pw_biasa"][i]:
                    if user == data_pengguna["user_biasa"][i]:
                        awal_1 = True
                        input("\n(Hanya password yang salah, ketuk enter untuk kembali)")
                        break
                
            if awal_1 == False:
                input("\n(User tidak ditemukan, ketuk enter untuk login kembali)")

    elif pilihan_1 == "2":
        os.system("cls")
        print("=== Login Sebagai Admin ===\n")
        user = input("Masukkan username Anda = ").strip()
        pw = input("Masukkan password Anda = ").strip()

        while user != data_pengguna["user_admin"][0] or pw != data_pengguna["pw_admin"][0]:
            if user == "" or pw == "":
                input("\n(Masukkan karakter, ketuk enter untuk kembali)")
            elif user == data_pengguna["user_admin"][0]:
                input("\n(Hanya password yang salah, ketuk enter untuk kembali)")
            elif pw == data_pengguna["pw_admin"][0]:
                input("\n(Hanya username yang salah, ketuk enter untuk kembali)")
            else:
                input("\n(Username dan password Anda salah, ketuk enter untuk kembali)")
            os.system("cls")
            print("=== Login Sebagai Admin ===\n")
            user = input("Masukkan username Anda = ").strip()
            pw = input("Masukkan password Anda = ").strip()

        input("\n(Login berhasil, ketuk enter untuk lanjut)")
        login_admin = True
        awal_1 = True

    elif pilihan_1 == "3":
        os.system("cls")
        print("=== Menu Register ===\n")
        user = input("Masukkan username Anda = ").strip()
        pw = input("Masukkan password Anda = ").strip()

        while True:
            if user == "" or pw == "":
                input("\n(Masukkan karakter, ketuk enter untuk kembali)")
            elif user in data_pengguna["user_biasa"]:
                input("\n(Pengguna sudah ada, harap ganti username Anda)")
            else:
                break
            os.system("cls")
            print("=== Menu Register ===\n")
            user = input("Masukkan username Anda = ").strip()
            pw = input("Masukkan password Anda = ").strip()

        data_pengguna["user_biasa"].append(user)
        data_pengguna["pw_biasa"].append(pw)
        input("\n(Register berhasil, ketuk enter untuk login ulang)")

if login_admin:
    while login_admin:
        os.system("cls")
        print("=== Selamat Datang Tuan Admin ===\n")
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
            for i in range(len(data_pemain["gk_utama"])):
                print(f"    {i+1}. {data_pemain["gk_utama"][i]} (GK)")
            for i in range(len(data_pemain["df_utama"])):
                print(f"    {i+2}. {data_pemain["df_utama"][i]} (DF)")
            for i in range(len(data_pemain["mf_utama"])):
                print(f"    {i+7}. {data_pemain["mf_utama"][i]} (MF)")
            for i in range(len(data_pemain["fw_utama"])):
                print(f"    {i+10}. {data_pemain["fw_utama"][i]} (FW)")
            
            print("\nCadangan:")
            for i in range(len(data_pemain["gk_cadangan"])):
                print(f"    {i+1}. {data_pemain["gk_cadangan"][i]} (GK)")
            for i in range(len(data_pemain["df_cadangan"])):
                print(f"    {i+1+len(data_pemain["gk_cadangan"])}. {data_pemain["df_cadangan"][i]} (DF)")
            for i in range(len(data_pemain["mf_cadangan"])):
                print(f"    {i+1+len(data_pemain["gk_cadangan"] + data_pemain["df_cadangan"])}. {data_pemain["mf_cadangan"][i]} (MF)")
            for i in range(len(data_pemain["fw_cadangan"])):
                print(f"    {i+1+len(data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"])}. {data_pemain["fw_cadangan"][i]} (FW)")
            
            input("\n(Ketuk enter untuk kembali memilih menu)")

        elif pilihan_2 == "2":
            while True:
                os.system("cls")
                print("Starting:")
                for i in range(len(data_pemain["gk_utama"])):
                    print(f"    {i+1}. {data_pemain["gk_utama"][i]} (GK)")
                for i in range(len(data_pemain["df_utama"])):
                    print(f"    {i+2}. {data_pemain["df_utama"][i]} (DF)")
                for i in range(len(data_pemain["mf_utama"])):
                    print(f"    {i+7}. {data_pemain["mf_utama"][i]} (MF)")
                for i in range(len(data_pemain["fw_utama"])):
                    print(f"    {i+10}. {data_pemain["fw_utama"][i]} (FW)")
                    
                print("\nCadangan:")
                for i in range(len(data_pemain["gk_cadangan"])):
                    print(f"    {i+1}. {data_pemain["gk_cadangan"][i]} (GK)")
                for i in range(len(data_pemain["df_cadangan"])):
                    print(f"    {i+1+len(data_pemain["gk_cadangan"])}. {data_pemain["df_cadangan"][i]} (DF)")
                for i in range(len(data_pemain["mf_cadangan"])):
                    print(f"    {i+1+len(data_pemain["gk_cadangan"] + data_pemain["df_cadangan"])}. {data_pemain["mf_cadangan"][i]} (MF)")
                for i in range(len(data_pemain["fw_cadangan"])):
                    print(f"    {i+1+len(data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"])}. {data_pemain["fw_cadangan"][i]} (FW)")
                pemain_tambahan = input("\nMasukkan nama pemain = ").strip()

                if pemain_tambahan in cek_pemain:
                    input("\n(Pemain sudah ada di line up, ketuk enter untuk menambah kembali)")
                    continue

                pilihan_3 = input("Pilih lini yang ingin ditambah (GK/DF/MF/FW) = ").strip().upper()
                if pilihan_3 == "GK":
                    data_pemain["gk_cadangan"].append(pemain_tambahan)
                elif pilihan_3 == "DF":
                    data_pemain["df_cadangan"].append(pemain_tambahan)
                elif pilihan_3 == "MF":
                    data_pemain["mf_cadangan"].append(pemain_tambahan)
                elif pilihan_3 == "FW":
                    data_pemain["fw_cadangan"].append(pemain_tambahan)
                else:
                    input("\n(Input tidak valid, ketuk enter untuk kembali)")
                    continue
                
                print(f"(Sukses menambahkan {pemain_tambahan} ke dalam lini {pilihan_3})")
                input("\n(Ketuk enter untuk kembali memilih menu)")
                semua_pemain = data_pemain["gk_utama"] + data_pemain["df_utama"] + data_pemain["mf_utama"] + data_pemain["fw_utama"] + data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"] + data_pemain["fw_cadangan"]
                cek_pemain = set(semua_pemain)
                break

        elif pilihan_2 == "3":
            while True:
                os.system("cls")
                print("Starting:")
                for i in range(len(data_pemain["gk_utama"])):
                    print(f"    {i+1}. {data_pemain["gk_utama"][i]} (GK)")
                for i in range(len(data_pemain["df_utama"])):
                    print(f"    {i+2}. {data_pemain["df_utama"][i]} (DF)")
                for i in range(len(data_pemain["mf_utama"])):
                    print(f"    {i+7}. {data_pemain["mf_utama"][i]} (MF)")
                for i in range(len(data_pemain["fw_utama"])):
                    print(f"    {i+10}. {data_pemain["fw_utama"][i]} (FW)")
                pemain_tukar = input("\nMasukkan nama pemain = ").strip()

                if pemain_tukar in cek_pemain:
                    input("\n(Pemain sudah ada di line up, ketuk enter untuk menambah kembali)")
                    continue

                pilihan_3 = input("Pilih lini yang ingin diganti (GK/DF/MF/FW) = ").strip().upper()
                if pilihan_3 == "GK":
                    for i in range(len(data_pemain["gk_utama"])):
                        print(f"    {i+1}. {data_pemain["gk_utama"][i]} (GK)")
                    pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_diganti = int(pemain) - 1
                    if pemain_diganti > len(data_pemain["gk_utama"]) - 1 or pemain_diganti < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        data_pemain["gk_utama"][pemain_diganti] = pemain_tukar
                        break
                elif pilihan_3 == "DF":
                    for i in range(len(data_pemain["df_utama"])):
                        print(f"    {i+1}. {data_pemain["df_utama"][i]} (DF)")
                    pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_diganti = int(pemain) - 1
                    if pemain_diganti > len(data_pemain["df_utama"]) - 1 or pemain_diganti < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        data_pemain["df_utama"][pemain_diganti] = pemain_tukar
                        break
                elif pilihan_3 == "MF":
                    for i in range(len(data_pemain["mf_utama"])):
                        print(f"    {i+1}. {data_pemain["mf_utama"][i]} (MF)")
                    pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_diganti = int(pemain) - 1
                    if pemain_diganti > len(data_pemain["mf_utama"]) - 1 or pemain_diganti < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        data_pemain["mf_utama"][pemain_diganti] = pemain_tukar
                        break
                elif pilihan_3 == "FW":
                    for i in range(len(data_pemain["fw_utama"])):
                        print(f"    {i+1}. {data_pemain["fw_utama"][i]} (FW)")
                    pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_diganti = int(pemain) - 1
                    if pemain_diganti > len(data_pemain["fw_utama"]) - 1 or pemain_diganti < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        data_pemain["fw_utama"][pemain_diganti] = pemain_tukar
                        break
                else:
                    input("\n(Input tidak valid, ketuk enter untuk kembali)")
                    continue
            
            print(f"(Sukses mengganti pemain dengan {pemain_tukar})")
            input("\n(Ketuk enter untuk kembali memilih menu)")
            semua_pemain = data_pemain["gk_utama"] + data_pemain["df_utama"] + data_pemain["mf_utama"] + data_pemain["fw_utama"] + data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"] + data_pemain["fw_cadangan"]
            cek_pemain = set(semua_pemain)
                
        
        elif pilihan_2 == "4":
            while True:
                os.system("cls")
                print("Cadangan:")
                for i in range(len(data_pemain["gk_cadangan"])):
                    print(f"    {i+1}. {data_pemain["gk_cadangan"][i]} (GK)")
                for i in range(len(data_pemain["df_cadangan"])):
                    print(f"    {i+2}. {data_pemain["df_cadangan"][i]} (DF)")
                for i in range(len(data_pemain["mf_cadangan"])):
                    print(f"    {i+7}. {data_pemain["mf_cadangan"][i]} (MF)")
                for i in range(len(data_pemain["fw_cadangan"])):
                    print(f"    {i+10}. {data_pemain["fw_cadangan"][i]} (FW)")
                pemain_tukar = input("\nMasukkan nama pemain = ").strip()

                if pemain_tukar in cek_pemain:
                    input("\n(Pemain sudah ada di line up, ketuk enter untuk menambah kembali)")
                    continue

                pilihan_3 = input("Pilih lini yang ingin diganti (GK/DF/MF/FW) = ").strip().upper()
                if pilihan_3 == "GK":
                    for i in range(len(data_pemain["gk_cadangan"])):
                        print(f"    {i+1}. {data_pemain["gk_cadangan"][i]} (GK)")
                    pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_diganti = int(pemain) - 1
                    if pemain_diganti > len(data_pemain["gk_cadangan"]) - 1 or pemain_diganti < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        data_pemain["gk_cadangan"][pemain_diganti] = pemain_tukar
                        break
                elif pilihan_3 == "DF":
                    for i in range(len(data_pemain["df_cadangan"])):
                        print(f"    {i+1}. {data_pemain["df_cadangan"][i]} (DF)")
                    pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_diganti = int(pemain) - 1
                    if pemain_diganti > len(data_pemain["df_cadangan"]) - 1 or pemain_diganti < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        data_pemain["df_cadangan"][pemain_diganti] = pemain_tukar
                        break
                elif pilihan_3 == "MF":
                    for i in range(len(data_pemain["mf_cadangan"])):
                        print(f"    {i+1}. {data_pemain["mf_cadangan"][i]} (MF)")
                    pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_diganti = int(pemain) - 1
                    if pemain_diganti > len(data_pemain["mf_cadangan"]) - 1 or pemain_diganti < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        data_pemain["mf_cadangan"][pemain_diganti] = pemain_tukar
                        break
                elif pilihan_3 == "FW":
                    for i in range(len(data_pemain["fw_cadangan"])):
                        print(f"    {i+1}. {data_pemain["fw_cadangan"][i]} (FW)")
                    pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_diganti = int(pemain) - 1
                    if pemain_diganti > len(data_pemain["fw_cadangan"]) - 1 or pemain_diganti < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        data_pemain["fw_cadangan"][pemain_diganti] = pemain_tukar
                        break
                else:
                    input("\n(Input tidak valid, ketuk enter untuk kembali)")
                    continue
        
            print(f"(Sukses mengganti pemain dengan {pemain_tukar})")
            input("\n(Ketuk enter untuk kembali memilih menu)")
            semua_pemain = data_pemain["gk_utama"] + data_pemain["df_utama"] + data_pemain["mf_utama"] + data_pemain["fw_utama"] + data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"] + data_pemain["fw_cadangan"]
            cek_pemain = set(semua_pemain)
                
        elif pilihan_2 == "5":
            while True:
                os.system("cls")
                print("Cadangan:")
                for i in range(len(data_pemain["gk_cadangan"])):
                    print(f"    {i+1}. {data_pemain["gk_cadangan"][i]} (GK)")
                for i in range(len(data_pemain["df_cadangan"])):
                    print(f"    {i+2}. {data_pemain["df_cadangan"][i]} (DF)")
                for i in range(len(data_pemain["mf_cadangan"])):
                    print(f"    {i+7}. {data_pemain["mf_cadangan"][i]} (MF)")
                for i in range(len(data_pemain["fw_cadangan"])):
                    print(f"    {i+10}. {data_pemain["fw_cadangan"][i]} (FW)")
                
                pilihan_3 = input("\nPilih lini yang ingin dihapus (GK/DF/MF/FW) = ").strip().upper()
                if pilihan_3 == "GK":
                    for i in range(len(data_pemain["gk_cadangan"])):
                        print(f"    {i+1}. {data_pemain["gk_cadangan"][i]} (GK)")
                    pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_dihapus = int(pemain) -1 
                    if pemain_dihapus > len(data_pemain["gk_cadangan"]) -1 or pemain_dihapus < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        panggil_pemain = data_pemain["gk_cadangan"][pemain_dihapus]
                        del data_pemain["gk_cadangan"][pemain_dihapus]
                        break
                elif pilihan_3 == "DF":
                    for i in range(len(data_pemain["df_cadangan"])):
                        print(f"    {i+1}. {data_pemain["df_cadangan"][i]} DF)")
                    pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_dihapus = int(pemain) -1
                    if pemain_dihapus > len(data_pemain["df_cadangan"]) -1 or pemain_dihapus < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        panggil_pemain = data_pemain["df_cadangan"][pemain_dihapus]
                        del data_pemain["df_cadangan"][pemain_dihapus]
                        break
                elif pilihan_3 == "MF":
                    for i in range(len(data_pemain["mf_cadangan"])):
                        print(f"    {i+1}. {data_pemain["mf_cadangan"][i]} (MF)")
                    pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_dihapus = int(pemain) -1
                    if pemain_dihapus > len(data_pemain["mf_cadangan"]) -1 or pemain_dihapus < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        panggil_pemain = data_pemain["mf_cadangan"][pemain_dihapus]
                        del data_pemain["mf_cadangan"][pemain_dihapus]
                        break
                elif pilihan_3 == "FW":
                    for i in range(len(data_pemain["fw_cadangan"])):
                        print(f"    {i+1}. {data_pemain["fw_cadangan"][i]} (FW)")
                    pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
                    if not pemain.isdigit():
                        input("\n(Input tidak valid, ketuk enter untuk kembali)")
                        continue
                    pemain_dihapus = int(pemain) -1
                    if pemain_dihapus > len(data_pemain["fw_cadangan"]) -1 or pemain_dihapus < 0:
                        input("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
                        continue
                    else:
                        panggil_pemain = data_pemain["fw_cadangan"][pemain_dihapus]
                        del data_pemain["fw_cadangan"][pemain_dihapus]
                        break
                else:
                    input("\n(Input tidak valid, ketuk enter untuk kembali)")
                    continue
            
            print(f"(Sukses menghapus {panggil_pemain})")
            input("\n(Ketuk enter untuk kembali memilih menu)")
            semua_pemain = data_pemain["gk_utama"] + data_pemain["df_utama"] + data_pemain["mf_utama"] + data_pemain["fw_utama"] + data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"] + data_pemain["fw_cadangan"]
            cek_pemain = set(semua_pemain)
                
        elif pilihan_2 == "6":
            login_admin = False

        else:
            input("\n(Input tidak valid, ketuk enter untuk kembali)")

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
            for i in range(len(data_pemain["gk_utama"])):
                print(f"    {i+1}. {data_pemain["gk_utama"][i]} (GK)")
            for i in range(len(data_pemain["df_utama"])):
                print(f"    {i+2}. {data_pemain["df_utama"][i]} (DF)")
            for i in range(len(data_pemain["mf_utama"])):
                print(f"    {i+7}. {data_pemain["mf_utama"][i]} (MF)")
            for i in range(len(data_pemain["fw_utama"])):
                print(f"    {i+10}. {data_pemain["fw_utama"][i]} (FW)")
            
            print("\nCadangan:")
            for i in range(len(data_pemain["gk_cadangan"])):
                print(f"    {i+1}. {data_pemain["gk_cadangan"][i]} (GK)")
            for i in range(len(data_pemain["df_cadangan"])):
                print(f"    {i+1+len(data_pemain["gk_cadangan"])}. {data_pemain["df_cadangan"][i]} (DF)")
            for i in range(len(data_pemain["mf_cadangan"])):
                print(f"    {i+1+len(data_pemain["gk_cadangan"] + data_pemain["df_cadangan"])}. {data_pemain["mf_cadangan"][i]} (MF)")
            for i in range(len(data_pemain["fw_cadangan"])):
                print(f"    {i+1+len(data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"])}. {data_pemain["fw_cadangan"][i]} (FW)")
            
            input("\n(Ketuk enter untuk kembali memilih menu)")

        elif pilihan_2 == "2":
            login_user = False

        else:
            input("\n(Input tidak valid, ketuk enter untuk kembali)")

os.system("cls")
print(f"✨ Terima kasih atas waktunya, {user}. Sampai jumpa di lain kesempatan! Selamat tinggal. 👋")