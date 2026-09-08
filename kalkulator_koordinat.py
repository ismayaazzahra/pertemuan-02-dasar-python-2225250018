"""
Tugas Utama - Kalkulator Koordinat Dua Titik
Algoritma dan Pemrograman - Pertemuan 2
Nama   : (ismaya catur dewi azzahra)
NIM    : (2225250018)
Kelas  : 2 A

Deskripsi:
Program menerima koordinat dua buah titik, A(x1, y1) dan B(x2, y2),
sebagai bilangan desimal (float). Program kemudian menghitung
perubahan koordinat (dx, dy), jarak Euclidean antara kedua titik,
dan koordinat titik tengah di antara keduanya. Seluruh hasil
ditampilkan dengan dua angka desimal.

Catatan: sesuai spesifikasi tugas, program ini belum menggunakan
struktur seleksi (if), perulangan (loop), fungsi buatan sendiri,
maupun pustaka eksternal karena materi tersebut belum dibahas pada
pertemuan ini.
"""

print("KALKULATOR KOORDINAT DUA TITIK")

x1 = float(input("x titik A: "))
y1 = float(input("y titik A: "))
x2 = float(input("x titik B: "))
y2 = float(input("y titik B: "))

dx = x2 - x1
dy = y2 - y1

jarak = ((dx ** 2) + (dy ** 2)) ** 0.5

titik_tengah_x = (x1 + x2) / 2
titik_tengah_y = (y1 + y2) / 2

print(f"Titik A       : ({x1:.2f}, {y1:.2f})")
print(f"Titik B       : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan     : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B  : {jarak:.2f}")
print(f"Titik tengah  : ({titik_tengah_x:.2f}, {titik_tengah_y:.2f})")