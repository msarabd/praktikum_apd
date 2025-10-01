list = [27, 33, 46, 55, 67, 92]
print("List data =", list[0:])

print('\n"LIST DATA SETELAH DIKONVERSI"')
suhu1_f = 9/5 * list[0] + 32
print("suhu 1 =", suhu1_f, "fahrenheit")

suhu2_f = 9/5 * list[1] + 32
print("suhu 2 =", suhu2_f, "fahrenheit")

suhu3_k = list[-4] + 273.15
print("suhu 3 =", suhu3_k, "kelvin")

suhu4_k = list[-3] + 273.15
print("suhu 4 =", suhu4_k, "kelvin")

suhu5_r = 4/5 * list [-2]
print("suhu 5 =", suhu5_r, "reamur")

suhu6_r = 4/5 * list [-1]
print("suhu 6 =", suhu6_r, "reamur")

jumlah = suhu1_f + suhu2_f + suhu3_k + suhu4_k + suhu5_r + suhu6_r
print("\nJumlah =", jumlah)


rata2 = jumlah/6
print("Rata - rata =", rata2)

NIM = 67
print("NIM =", NIM)
boolean = NIM < rata2
print("Boolean =", boolean)