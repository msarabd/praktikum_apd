# # list_mahasiswa = [74, "Nama", "NIM"]
# # print(list_mahasiswa)

# # creat list
# praktikum = ["Mahasiswa", 20, True, 45.10, ["APD",25]]
# print(praktikum)
# print(praktikum[4][1])

# # update list
# praktikum.append("Indonesia")
# print(praktikum)

# praktikum.insert(2, 6)
# print(praktikum)

# praktikum[2] = "AI"
# print(praktikum)

# # del dan pop
# del praktikum[2]
# print(praktikum)

# # kosong = praktikum.pop(4)
# # print(praktikum)
# # print(kosong)

# kosong = praktikum[4].pop(0)
# print(praktikum)
# print(kosong)

# praktikum.remove("Indonesia")
# print(praktikum)

# # start, stop, step
# print(praktikum[0:1000:3])

# for item in praktikum[0:4:3]:
#     print(item, end=",")

# for i in range(len(praktikum)):
#     print(i+1, ":", praktikum[i])
    
# maha = [3, 4]
# hasil = maha + praktikum
# print(hasil)

# hasil = maha*4
# print(hasil)

# for i in maha:
#     print(i*3)

# kelas = [
# ["Ridho", "Lian", "Nabil"],
# ["Daffa", "Dante", "Santoso"],
# ["Pernanda", "Riyadi", "Ahnaf"],
# ]

# print(kelas[0][1])

# tuple
# anggota = ("riyadi", 20, True, 3.96, ["APD",25],("samarinda",12))

# langgota = list(anggota)
# langgota.append("mahdi")

# anggota = list(langgota)
# print(anggota)

tugas = ('rangkuman', 'arduino','scrapping')
# beri variabel setiap values
(PTI, orsikom, basisdata) = tugas
print(PTI)
print(orsikom)
print(basisdata)