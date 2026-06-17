# ============================================================
#   PROGRAM PENGOLAHAN NILAI 30 SISWA
#   Tugas Algoritma & Pemrograman
#
#   Soal 2 : Menghitung rata-rata nilai siswa
#   Soal 3 : Mencari nilai tertinggi dan terendah
# ============================================================

# --------------------------------------------------
# KONSEP: Array / List
# Array digunakan untuk menyimpan banyak nilai dalam
# satu variabel. Contoh: nilai[0], nilai[1], ..., nilai[29]
# Lebih efisien daripada membuat 30 variabel terpisah.
# --------------------------------------------------

JUMLAH_SISWA = 30  # Konstanta jumlah siswa


# ==========================================================
#  FUNGSI 1: Input dan simpan nilai siswa ke dalam array
# ==========================================================
def input_nilai():
    nilai = []  # Membuat array kosong

    for i in range(JUMLAH_SISWA):          # Perulangan 0 s.d. 29 (30 kali)
        while True:                         # Loop validasi input
            try:
                n = float(input(f"Masukkan nilai siswa ke-{i + 1}: "))
                if 0 <= n <= 100:           # Validasi rentang nilai
                    nilai.append(n)         # Tambahkan nilai ke array
                    break
                else:
                    print("  [!] Nilai harus antara 0 - 100. Coba lagi.")
            except ValueError:
                print("  [!] Input tidak valid. Masukkan angka.")

    return nilai  # Kembalikan array berisi 30 nilai


# ==========================================================
#  FUNGSI 2 (Soal 2): Menghitung rata-rata dengan perulangan
#
#  Pseudocode:
#    total    ← 0
#    FOR setiap n dalam array nilai:
#        total ← total + n
#    rata_rata ← total / JUMLAH_SISWA
#    RETURN rata_rata
# ==========================================================
def hitung_rata_rata(nilai):
    total = 0                          # Akumulator dimulai dari 0

    for n in nilai:                    # Iterasi setiap elemen array
        total = total + n              # Tambahkan ke total (akumulasi)

    rata_rata = total / JUMLAH_SISWA   # Bagi total dengan jumlah siswa
    return rata_rata


# ==========================================================
#  FUNGSI 3 (Soal 3): Mencari nilai tertinggi & terendah
#                      menggunakan perulangan
#
#  Pseudocode:
#    tertinggi ← nilai[0]   (asumsikan elemen pertama sebagai max)
#    terendah  ← nilai[0]   (asumsikan elemen pertama sebagai min)
#    FOR i dari 1 sampai 29:
#        IF nilai[i] > tertinggi THEN
#            tertinggi ← nilai[i]
#        IF nilai[i] < terendah THEN
#            terendah  ← nilai[i]
#    RETURN tertinggi, terendah
# ==========================================================
def cari_tertinggi_terendah(nilai):
    tertinggi = nilai[0]   # Anggap nilai pertama sebagai yang tertinggi
    terendah  = nilai[0]   # Anggap nilai pertama sebagai yang terendah

    for i in range(1, JUMLAH_SISWA):   # Mulai dari indeks ke-1 (sudah cek ke-0)
        if nilai[i] > tertinggi:        # Jika lebih besar dari tertinggi saat ini
            tertinggi = nilai[i]        #   → perbarui tertinggi
        if nilai[i] < terendah:         # Jika lebih kecil dari terendah saat ini
            terendah  = nilai[i]        #   → perbarui terendah

    return tertinggi, terendah


# ==========================================================
#  FUNGSI 4: Menampilkan hasil akhir
# ==========================================================
def tampilkan_hasil(nilai, rata_rata, tertinggi, terendah):
    print("\n" + "=" * 42)
    print("      HASIL PENGOLAHAN NILAI SISWA")
    print("=" * 42)
    print(f"  Jumlah Siswa    : {len(nilai)} orang")
    print(f"  Rata-rata Nilai : {rata_rata:.2f}")      # 2 angka desimal
    print(f"  Nilai Tertinggi : {tertinggi:.0f}")
    print(f"  Nilai Terendah  : {terendah:.0f}")
    print("=" * 42)


# ==========================================================
#  PROGRAM UTAMA (Main)
#  Urutan eksekusi:
#    1. Tampilkan header
#    2. Input semua nilai → simpan ke array
#    3. Hitung rata-rata  (Soal 2)
#    4. Cari tertinggi & terendah (Soal 3)
#    5. Tampilkan hasil
# ==========================================================
def main():
    print("=" * 42)
    print("   PROGRAM PENGOLAHAN NILAI 30 SISWA")
    print("=" * 42)

    # Langkah 1 — Input nilai, simpan ke array
    nilai = input_nilai()

    # Langkah 2 — Soal 2: Hitung rata-rata menggunakan perulangan
    rata_rata = hitung_rata_rata(nilai)

    # Langkah 3 — Soal 3: Cari tertinggi & terendah menggunakan perulangan
    tertinggi, terendah = cari_tertinggi_terendah(nilai)

    # Langkah 4 — Tampilkan semua hasil
    tampilkan_hasil(nilai, rata_rata, tertinggi, terendah)


if __name__ == "__main__":
    main()