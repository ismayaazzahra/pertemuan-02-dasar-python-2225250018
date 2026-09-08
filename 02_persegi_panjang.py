"""
Latihan 2 - Persegi Panjang
Algoritma dan Pemrograman - Pertemuan 2
Nama   : (ismaya catur dewi azzahra)
NIM    : (2225250018)

Deskripsi:
Program menerima panjang dan lebar sebagai bilangan desimal (float),
lalu menghitung luas dan keliling persegi panjang, kemudian
menampilkan hasilnya dengan dua angka desimal beserta satuannya.
"""

panjang = float(input("Panjang: "))
lebar = float(input("Lebar: "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas     = {luas:.2f} satuan persegi")
print(f"Keliling = {keliling:.2f} satuan panjang")