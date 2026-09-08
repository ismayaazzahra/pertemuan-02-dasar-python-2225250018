"""
Latihan 4 - Nilai Akhir
Algoritma dan Pemrograman - Pertemuan 2
Nama   : (ismaya catur dewi azzahra)
NIM    : (2225250018)

Deskripsi:
Program menerima nama mahasiswa beserta nilai tugas, UTS, dan UAS,
lalu menghitung nilai akhir menggunakan bobot 20% tugas, 30% UTS,
dan 50% UAS. Penentuan lulus/tidak lulus belum dilakukan pada
latihan ini karena struktur seleksi (if) belum menjadi materi
pertemuan ini.
"""

BOBOT_TUGAS = 0.20
BOBOT_UTS = 0.30
BOBOT_UAS = 0.50

nama = input("Nama: ")
nilai_tugas = float(input("Nilai tugas: "))
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))

nilai_akhir = (
    nilai_tugas * BOBOT_TUGAS
    + nilai_uts * BOBOT_UTS
    + nilai_uas * BOBOT_UAS
)

print(f"Nama         : {nama}")
print(f"Nilai akhir = {nilai_akhir:.2f}")