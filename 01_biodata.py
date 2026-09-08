"""
Latihan 1 - Biodata Terformat
Algoritma dan Pemrograman - Pertemuan 2
Nama   : (ismaya catur dewi azzahra)
NIM    : (2225250018)

Deskripsi:
Program menerima nama, NIM, kelas, dan tahun lahir dari pengguna,
lalu menghitung perkiraan umur berdasarkan konstanta TAHUN_SEKARANG,
kemudian menampilkan kartu biodata dengan format f-string.
"""

TAHUN_SEKARANG = 2026

nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun lahir: "))

umur = TAHUN_SEKARANG - tahun_lahir

print()
print(f"Nama  : {nama}")
print(f"NIM   : {nim}")
print(f"Kelas : {kelas}")
print(f"Umur  : sekitar {umur} tahun")