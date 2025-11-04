import os
from data import data_pengguna, data_pemain, semua_pemain, cek_pemain

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
                    return user, login_user, awal_1
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
        return user, login_admin, awal_1

def input_register():
    global data_pengguna
    global user
    
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
