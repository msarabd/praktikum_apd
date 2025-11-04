angka = 4

binder_angka = bin(angka)
print(binder_angka)

float_angka = float(angka)
print(float_angka)

num = int("42")
name = str(142)
data = list("123")
data_dict = dict(a=2, b=3)

print(num)
print(name)
print(data)
print(data_dict)

print(abs(-4))

list_angka = [10, 30, 15, 4]
max_angka = max(list_angka)
print("Nilai maksimum dari list_angka =", max_angka)

angka = 3.4567
print(round(angka))
print(round(angka, 2)) # ambil 2 digit di belakang koma

penjumlahan = sum([1, 2]) # fungsi sum harus pakai tipe data array
print(penjumlahan)

print(pow(2, 3))
print(divmod(10, 3)) # hasil bagi, sisa bagi

from datetime import datetime
print(datetime.now())
print(dir(datetime)) # dir untuk menampilkan apa aja yang bisa dilakukan di library tersebut

from prettytable import prettytable

