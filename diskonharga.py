"""
Tugas Pertemuan 1 - Algoritma dan Pemrograman
Nama   : Ismaya Catur Dewi Azzahra
NIM    : 2225250018
Judul  : Menghitung Harga Barang Setelah Diskon (Aritmetika Sosial)

Deskripsi:
Program ini menerima harga awal suatu barang dan besar persentase
diskon yang diberikan, kemudian menghitung nilai diskon (potongan
harga) dan harga akhir yang harus dibayar pembeli.
"""


def hitung_diskon(harga_awal, persen_diskon):
    """
    Menghitung nilai diskon dan harga akhir setelah diskon.

    Parameter:
        harga_awal (float): harga barang sebelum diskon
        persen_diskon (float): besar diskon dalam persen (misal 20 untuk 20%)

    Mengembalikan:
        tuple: (nilai_diskon, harga_akhir)
    """
    nilai_diskon = (persen_diskon / 100) * harga_awal
    harga_akhir = harga_awal - nilai_diskon
    return nilai_diskon, harga_akhir


def main():
    print("=== PROGRAM PENGHITUNG HARGA SETELAH DISKON ===")
    harga_awal = float(input("Masukkan harga awal barang (Rp): "))
    persen_diskon = float(input("Masukkan besar diskon (%): "))

    nilai_diskon, harga_akhir = hitung_diskon(harga_awal, persen_diskon)

    print(f"Harga Awal   : Rp{harga_awal:,.0f}")
    print(f"Diskon       : {persen_diskon}%  (Rp{nilai_diskon:,.0f})")
    print(f"Harga Akhir  : Rp{harga_akhir:,.0f}")


if __name__ == "__main__":
    main()