import os
os.system("cls")

data_pengguna = {
    "user_admin" : ["admin"],
    "pw_admin" : ["admin123"],
    "user_biasa" : ["mahdi"],
    "pw_biasa" : ["067"]
}

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
login_admin = False
login_user = False

def input_user():
    global awal_1
    global login_user
    global user

    ulang_1 = False
    while ulang_1 == False:
        awal_1 = False
        os.system("cls")
        print("=== Login Sebagai User Biasa ===\n")
        
        try:
            user = input("Masukkan username Anda = ").strip()
            pw = input("Masukkan password Anda = ").strip()

            if user == "" or pw == "":
                raise ValueError("\n(Masukkan karakter, tekan enter untuk login kembali)")
                
            for i in range(len(data_pengguna["user_biasa"])):
                if user == data_pengguna["user_biasa"][i] and pw == data_pengguna["pw_biasa"][i]:
                    input("\n(Login berhasil, ketuk enter untuk lanjut)")
                    login_user = True
                    ulang_1 = True
                    awal_1 = True
                    break
                elif user == data_pengguna["user_biasa"][i]: 
                    awal_1 = True
                    raise ValueError("\n(Password salah, ketuk enter untuk kembali)")
                
            if awal_1 == False:
                raise ValueError("\n(User tidak ditemukan, ketuk enter untuk login kembali)")
        
        except Exception as e:
            input(e)
            continue

def input_admin():
    global user
    global login_admin
    global awal_1

    while True:
        os.system("cls")
        print("=== Login Sebagai Admin ===\n")

        try:
            user = input("Masukkan username Anda = ").strip()
            pw = input("Masukkan password Anda = ").strip()

            if user != data_pengguna["user_admin"][0] or pw != data_pengguna["pw_admin"][0]:
                if user == "" or pw == "":
                    raise ValueError("\n(Masukkan karakter, ketuk enter untuk kembali)")
                elif user == data_pengguna["user_admin"][0]:
                    raise ValueError("\n(Password salah, ketuk enter untuk kembali)")
                elif pw == data_pengguna["pw_admin"][0]:
                    raise ValueError("\n(Username salah, ketuk enter untuk kembali)")
                else:
                    raise ValueError("\n(Username dan password salah, ketuk enter untuk kembali)")
    
        except Exception as e:
            input(e)
            continue
    
        input("\n(Login berhasil, ketuk enter untuk lanjut)")
        login_admin = True
        awal_1 = True
        break

def user_register():
    global data_pengguna

    while True:
        os.system("cls")
        print("=== Menu Register ===\n")

        try:
            user = input("Masukkan username Anda = ").strip()
            pw = input("Masukkan password Anda = ").strip()

            if user == "" or pw == "":
                raise ValueError("\n(Masukkan karakter, ketuk enter untuk kembali)")
            elif user in data_pengguna["user_biasa"]:
                raise ValueError("\n(Pengguna sudah ada, harap ganti username Anda)")
        
        except Exception as e:
            input(e)
            continue

        data_pengguna["user_biasa"].append(user)
        data_pengguna["pw_biasa"].append(pw)
        input("\n(Register berhasil, ketuk enter untuk login ulang)")
        break

def tampil_starting():
    print("Starting:")
    for i in range(len(data_pemain["gk_utama"])):
        print(f"    {i+1}. {data_pemain["gk_utama"][i]} (GK)")
    for i in range(len(data_pemain["df_utama"])):
        print(f"    {i+2}. {data_pemain["df_utama"][i]} (DF)")
    for i in range(len(data_pemain["mf_utama"])):
        print(f"    {i+7}. {data_pemain["mf_utama"][i]} (MF)")
    for i in range(len(data_pemain["fw_utama"])):
        print(f"    {i+10}. {data_pemain["fw_utama"][i]} (FW)")

def tampil_cadangan():
    print("Cadangan:")
    for i in range(len(data_pemain["gk_cadangan"])):
        print(f"    {i+1}. {data_pemain["gk_cadangan"][i]} (GK)")
    for i in range(len(data_pemain["df_cadangan"])):
        print(f"    {i+1+len(data_pemain["gk_cadangan"])}. {data_pemain["df_cadangan"][i]} (DF)")
    for i in range(len(data_pemain["mf_cadangan"])):
        print(f"    {i+1+len(data_pemain["gk_cadangan"] + data_pemain["df_cadangan"])}. {data_pemain["mf_cadangan"][i]} (MF)")
    for i in range(len(data_pemain["fw_cadangan"])):
        print(f"    {i+1+len(data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"])}. {data_pemain["fw_cadangan"][i]} (FW)")

def tambah_pemain():
    global data_pemain
    global semua_pemain
    global cek_pemain
    
    os.system("cls")
    tampil_starting()
    print()
    tampil_cadangan()
    try:
        pemain_tambahan = input("\nMasukkan nama pemain = ").strip()

        if pemain_tambahan == "":
            raise ValueError("\n(Masukkan karakter, ketuk enter untuk kembali)")
        elif pemain_tambahan in cek_pemain:
            raise ValueError("\n(Pemain sudah ada di line up, ketuk enter untuk menambah kembali)") # butuh perbaikan ini

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
            raise ValueError("\n(Input tidak valid, ketuk enter untuk kembali)")
    
    except Exception as e:
        input(e)
        return tambah_pemain()

    print(f"(Sukses menambahkan {pemain_tambahan} ke dalam lini {pilihan_3})")
    input("\n(Ketuk enter untuk kembali memilih menu)")
    semua_pemain = data_pemain["gk_utama"] + data_pemain["df_utama"] + data_pemain["mf_utama"] + data_pemain["fw_utama"] + data_pemain["gk_cadangan"] + data_pemain["df_cadangan"] + data_pemain["mf_cadangan"] + data_pemain["fw_cadangan"]
    cek_pemain = set(semua_pemain)

def ganti_pemain(gk_status, df_status, mf_status, fw_status):
    global pemain_tukar
    global data_pemain
    global ulang_2
    
    ulang_2 = False
    os.system("cls")

    if pilihan_2 == "3":
        tampil_starting()
    else:
        tampil_cadangan()

    try:
        pemain_tukar = input("\nMasukkan nama pemain = ").strip()

        if pemain_tukar == "":
            raise ValueError("\n(Masukkan karakter, ketuk enter untuk kembali)")
        elif pemain_tukar in cek_pemain:
            raise ValueError("\n(Pemain sudah ada di line up, ketuk enter untuk menambah kembali)")

        pilihan_3 = input("Pilih lini yang ingin diganti (GK/DF/MF/FW) = ").strip().upper()
        if pilihan_3 == "GK":
            for i in range(len(data_pemain[gk_status])):
                print(f"    {i+1}. {data_pemain[gk_status][i]} (GK)")
            pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_diganti = int(pemain) - 1
            if pemain_diganti > len(data_pemain[gk_status]) - 1 or pemain_diganti < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                data_pemain[gk_status][pemain_diganti] = pemain_tukar
                ulang_2 = True
                return pemain_tukar
        elif pilihan_3 == "DF":
            for i in range(len(data_pemain[df_status])):
                print(f"    {i+1}. {data_pemain[df_status][i]} (DF)")
            pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_diganti = int(pemain) - 1
            if pemain_diganti > len(data_pemain[df_status]) - 1 or pemain_diganti < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                data_pemain[df_status][pemain_diganti] = pemain_tukar
                ulang_2 = True
                return pemain_tukar
        elif pilihan_3 == "MF":
            for i in range(len(data_pemain[mf_status])):
                print(f"    {i+1}. {data_pemain[mf_status][i]} (MF)")
            pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_diganti = int(pemain) - 1
            if pemain_diganti > len(data_pemain[mf_status]) - 1 or pemain_diganti < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                data_pemain[mf_status][pemain_diganti] = pemain_tukar
                ulang_2 = True
                return pemain_tukar
        elif pilihan_3 == "FW":
            for i in range(len(data_pemain[fw_status])):
                print(f"    {i+1}. {data_pemain[fw_status][i]} (FW)")
            pemain = input("\nMasukkan angka pemain yang ingin diganti = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_diganti = int(pemain) - 1
            if pemain_diganti > len(data_pemain[fw_status]) - 1 or pemain_diganti < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                data_pemain[fw_status][pemain_diganti] = pemain_tukar
                ulang_2 = True
                return pemain_tukar
        else:
            raise ValueError("\n(Input tidak valid, ketuk enter untuk kembali)")
    
    except Exception as e:
        input(e)
        return
    
def hapus_pemain():
    global data_pemain
    global ulang_2
    global panggil_pemain

    ulang_2 = False
    os.system("cls")
    tampil_cadangan()
    try:
        pilihan_3 = input("\nPilih lini yang ingin dihapus (GK/DF/MF/FW) = ").strip().upper()

        if pilihan_3 == "GK":
            for i in range(len(data_pemain["gk_cadangan"])):
                print(f"    {i+1}. {data_pemain["gk_cadangan"][i]} (GK)")
            pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_dihapus = int(pemain) -1 
            if pemain_dihapus > len(data_pemain["gk_cadangan"]) -1 or pemain_dihapus < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                panggil_pemain = data_pemain["gk_cadangan"][pemain_dihapus]
                del data_pemain["gk_cadangan"][pemain_dihapus]
                ulang_2 = True
                return
        elif pilihan_3 == "DF":
            for i in range(len(data_pemain["df_cadangan"])):
                print(f"    {i+1}. {data_pemain["df_cadangan"][i]} DF)")
            pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_dihapus = int(pemain) -1
            if pemain_dihapus > len(data_pemain["df_cadangan"]) -1 or pemain_dihapus < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                panggil_pemain = data_pemain["df_cadangan"][pemain_dihapus]
                del data_pemain["df_cadangan"][pemain_dihapus]
                ulang_2 = True
                return
        elif pilihan_3 == "MF":
            for i in range(len(data_pemain["mf_cadangan"])):
                print(f"    {i+1}. {data_pemain["mf_cadangan"][i]} (MF)")
            pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_dihapus = int(pemain) -1
            if pemain_dihapus > len(data_pemain["mf_cadangan"]) -1 or pemain_dihapus < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                panggil_pemain = data_pemain["mf_cadangan"][pemain_dihapus]
                del data_pemain["mf_cadangan"][pemain_dihapus]
                ulang_2 = True
                return
        elif pilihan_3 == "FW":
            for i in range(len(data_pemain["fw_cadangan"])):
                print(f"    {i+1}. {data_pemain["fw_cadangan"][i]} (FW)")
            pemain = input("\nMasukkan angka pemain yang ingin dihapus = ").strip()
            if not pemain.isdigit():
                raise ValueError("\n(Masukkan input berupa angka, ketuk enter untuk kembali)")
            pemain_dihapus = int(pemain) -1
            if pemain_dihapus > len(data_pemain["fw_cadangan"]) -1 or pemain_dihapus < 0:
                raise IndexError("\n(Pemain tidak ditemukan, ketuk enter untuk kembali)")
            else:
                panggil_pemain = data_pemain["fw_cadangan"][pemain_dihapus]
                del data_pemain["fw_cadangan"][pemain_dihapus]
                ulang_2 = True
                return 
        else:
            raise ValueError("\n(Input tidak valid, ketuk enter untuk kembali)")
    
    except Exception as e:
        input(e)
        return

def tampilan_ubah_pemain(par_pemain, pesan):
    global semua_pemain
    global cek_pemain

    print(f"(Sukses {pesan} {par_pemain})")
    input("\n(Ketuk enter untuk kembali memilih menu)")
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

    if pilihan_1 == "":
        input("\n(Masukkan karakter, ketuk enter untuk memilih kembali)")
        continue
    elif not pilihan_1.isdigit() or pilihan_1 == "0":
        input("\n(Masukkan angka sesuai pilihan, ketuk enter untuk memilih kembali)")
        continue
    
    elif pilihan_1 == "1":
        input_user()

    elif pilihan_1 == "2":
        input_admin()

    elif pilihan_1 == "3":
        user_register()

    else:
        input("\n(Input tidak valid, ketuk enter untuk memilih kembali)")

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
            tampil_starting()
            print()
            tampil_cadangan()
            input("\n(Ketuk enter untuk kembali memilih menu)")

        elif pilihan_2 == "2":
            tambah_pemain()

        elif pilihan_2 == "3":
            while True:
                ganti_pemain("gk_utama", "df_utama", "mf_utama", "fw_utama")
                if ulang_2 == True:
                    break
            
            tampilan_ubah_pemain(pemain_tukar, "mengganti pemain starting dengan")
                
        elif pilihan_2 == "4":
            while True:
                ganti_pemain("gk_cadangan", "df_cadangan", "mf_cadangan", "fw_cadangan")
                if ulang_2 == True:
                    break

            tampilan_ubah_pemain(pemain_tukar, "mengganti pemain cadangan dengan")
                
        elif pilihan_2 == "5":
            while True:
                hapus_pemain()
                if ulang_2 == True:
                    break

            tampilan_ubah_pemain(panggil_pemain, "menghapus")
                
        elif pilihan_2 == "6":
            login_admin = False

        else:
            input("\n(Input tidak valid, ketuk enter untuk kembali)")

elif login_user:
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
            tampil_starting()
            print()
            tampil_cadangan()
            input("\n(Ketuk enter untuk kembali memilih menu)")

        elif pilihan_2 == "2":
            login_user = False

        else:
            input("\n(Input tidak valid, ketuk enter untuk kembali)")

os.system("cls")
print(f"✨ Terima kasih atas waktunya, {user}. Sampai jumpa di lain kesempatan! Selamat tinggal. 👋")