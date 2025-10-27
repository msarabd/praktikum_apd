# def pesan_halo():
#     print("Halo akademik")
#     print("Indonesia")

# pesan_halo()

# x = 0 # variabel global
# def pertambahan():
#     x = x + 3 # variabel lokal
#     print(x)

# pertambahan()

# def segitiga(alas, tinggi):
#     luas = 1/2 * alas * tinggi
#     print(luas)

# segitiga(10, 2)

# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas

# def volume(sisi):
#     volume = luas_persegi(sisi) * sisi
#     print(volume)


# print(luas_persegi(4))
# print(volume(4))

# # membuat variabel global 
# Nama = "Hambali"

# Mata_Kuliah = "Algoritma dan Pemrograman Dasar" 
# # membuat variabel lokal 
# def info(): 
#     Nama = "Informatika" 
#     Mata_Kuliah = "Logika Informatika" 
#     # mengakses variabel lokal 
#     print("Prodi:", Nama) 
#     print("Mata Kuliah:", Mata_Kuliah)
 
# # mengakses variabel global 
# print("Prodi:", Nama) 
# print("Mata Kuliah:", Mata_Kuliah) 

# # memanggil fungsi info 
# info()

# def faktorial(n): 
#     # Basis (Base Case): Kondisi berhenti 
#     if n == 1 or n == 0: 
#         return 1 
#         # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri 
#     else: 
#         return n * faktorial(n - 1) 

# # Memanggil fungsi 
# hasil = faktorial(5) 
# print(f"Hasil dari 5! adalah: {hasil}")

# film = []
# # Fungsi untuk menampilkan semua data 
# def show_data(): 
#     if len(film) <= 0: 
#         print("Belum Ada data") 
#     else: 
#         print("ID | Judul Film") 
#         for indeks in range(len(film)): 
#             print(indeks, "|", film[indeks])

# show_data()

# try: 
#     angka = int(input('Masukkan Angka : ')) 
# except ValueError: 
#     print('input yang anda masukkan bukan Integer (angka)')
# else : 
#     print(f'Angka yang kamu input : {angka}')

try: 
    usn = input('Username yang diinginkan : ') 
    if len(usn) < 5: 
        raise ValueError('Nama Minimal Memiliki 5 karakter') 
except ValueError as e: 
    print(e)