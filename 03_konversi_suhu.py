"""
Latihan 3 - Konversi Suhu
Algoritma dan Pemrograman - Pertemuan 2
Nama   : (ismaya catur dewi azzahra)
NIM    : (2225250018)

Deskripsi:
Program menerima suhu dalam satuan Celsius sebagai bilangan desimal
(float), lalu mengonversinya ke satuan Fahrenheit dan Kelvin.
"""

KELVIN_OFFSET = 273.15

celsius = float(input("Suhu Celsius: "))

fahrenheit = (9 / 5) * celsius + 32
kelvin = celsius + KELVIN_OFFSET

print(f"Fahrenheit = {fahrenheit:.2f}")
print(f"Kelvin     = {kelvin:.2f}")