set_makanan = {"nasi", "nasi", "ayam", "sayur", "buah"}
set_minuman = {"air", "jus", "susu", "teh"}
print(set_makanan)

for minum in set_minuman:
    print("Minuman saya adalah", minum)

set_minuman.add("kopi")
print(set_minuman)

set_minuman.remove("teh") # saat menggunakan remove, value harus ada di set. Jika tidak ada, maka program akan error.
print(set_minuman)

set_minuman.discard("Air putih") # saat menggunakan discard, tidak apa jika tidak ditemukan value yang ingin dihapus.
print(set_minuman)

set_all = set_makanan.union(set_minuman)
print(set_all)

# union = menambahkan kedua set tanpa ada value yang sama (duplikasi)
set_makanan2 = {"ayam", "nasi", "mie ayam", "bakso"}
set_makanan_gabungan = set_makanan.union(set_makanan2)
print(set_makanan_gabungan)

# intersection = irisan antara kedua set
set_sama = set_makanan.intersection(set_makanan2)
print(set_sama) # output akan menampiilkan "set()" karena tidak ada value yang beririsan (himpunan kosong)

# difference = mencari value yang berbeda
set_makanan_saja = set_makanan.difference(set_makanan2)
print(set_makanan_saja) # hanya mencari value pada set_makanan yang tidak ada di set_makanan2

# update = menambahkan 2 set, mirip seperti union tetapi dia tidak perlu ditampung ke variabel baru
set_makanan.update(set_makanan2)

## dictionary
daftar_buku = {
"Buku1" : "Bumi Manusia",
"Buku2" : "Laut Bercerita"
}

print(daftar_buku["Buku1"])
print(daftar_buku)

Biodata = {
"Nama" : "Ananda Daffa Harahap",
"NIM" : 2409106050,
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" : True,
"Social Media" : {"IG" : "nimsugarr"}}

print(Biodata["KRS"][1])
print(Biodata["Social Media"]["IG"])
print(Biodata.get("Nama"))

Nilai = {
"Matematika": 80,
"B. Indonesia": 90,
"B. Inggris": 81,
"Kimia": 78,
"Fisika": 80
}
# Tanpa menggunakan items()
for i in Nilai:
    print(i)
print("") # pemisah

# Menggunakan items()
for i, j in Nilai.items():
    print(f"Nilai {i} anda adalah {j}")

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}

#Sebelum Ditambah
print(Film)
Film["Zombieland"] = "Comedy"
Film.update({"Hours" : "Thriller"})

#Setelah Ditambah
print(Film)

# mengubah item
Film["Sherlock Holmes"] = "Action"
Film.update({"The Conjuring" : "Tragedy"})
print(Film)

# menghapus item
data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
#Sebelum Dihapus
print(data)
del data["Nama"]
print(data)

#memanggil data yang telah dihapus
print(data.get("Nama"))

# pop
data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
#Sebelum Dihapus
print(data)
cache = data.pop("Nama")
#Setelah dihapus
print(data)
#memanggil data yang telah dihapus pada dictionary
print(data.get("Nama"))
#memanggil data yang telah dihapus pada variabel cache
print(cache)

# clear
data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}

#Sebelum Dihapus
print(data)
data.clear()
#Setelah dihapus
print(data)

# copy
buku = {
"Buku1" : "Bumi Manusia",
"Buku2" : "Laut Bercerita"
}

pinjam = buku.copy()
print("Dictionary yang telah disalin : ", pinjam)

# fromkeys
key = "apel", "jeruk", "mangga"
value = 1
buah = dict.fromkeys(key, value) # yang menjadi keys tidak boleh duplikat, sedangkan value boleh
print(buah)

#setdefault
print("")
Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)