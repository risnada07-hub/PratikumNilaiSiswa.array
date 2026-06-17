# PratikumNilaiSiswa.array
# ============================================================
#   README — Program Pengolahan Nilai 30 Siswa
#   Tugas Algoritma & Pemrograman
# ============================================================
#
#   Deskripsi:
#   Program Python untuk menyimpan nilai 30 siswa,
#   menghitung rata-rata, serta mencari nilai tertinggi
#   dan terendah menggunakan array dan perulangan.
#
# ============================================================
#   FITUR PROGRAM
# ============================================================
#
#   1. Input Nilai     — Menyimpan nilai 30 siswa ke dalam array
#   2. Rata-rata       — Menghitung rata-rata menggunakan perulangan (Soal 2)
#   3. Nilai Tertinggi — Mencari nilai terbesar menggunakan perulangan (Soal 3)
#   4. Nilai Terendah  — Mencari nilai terkecil menggunakan perulangan (Soal 3)
#   5. Validasi        — Memastikan nilai berada di rentang 0–100
#
# ============================================================
#   STRUKTUR FILE
# ============================================================
#
#   .
#   ├── nilai_siswa.py   # Source code utama (program lengkap)
#   └── README.py        # Dokumentasi ini
#
# ============================================================
#   CARA MENJALANKAN
# ============================================================
#
#   $ python nilai_siswa.py
#
#   Lalu masukkan nilai setiap siswa satu per satu saat diminta.
#
# ============================================================
#   PSEUDOCODE
# ============================================================
#
#   -- Soal 2: Menghitung Rata-rata --
#
#   MULAI
#     total     ← 0
#     FOR i dari 0 sampai 29:
#         total ← total + nilai[i]
#     rata_rata ← total / 30
#     TAMPILKAN rata_rata
#   SELESAI
#
#   -- Soal 3: Mencari Nilai Tertinggi dan Terendah --
#
#   MULAI
#     tertinggi ← nilai[0]
#     terendah  ← nilai[0]
#
#     FOR i dari 1 sampai 29:
#         IF nilai[i] > tertinggi THEN
#             tertinggi ← nilai[i]
#         IF nilai[i] < terendah THEN
#             terendah  ← nilai[i]
#
#     TAMPILKAN tertinggi, terendah
#   SELESAI
#
# ============================================================
#   CONTOH OUTPUT
# ============================================================
#
#   ==========================================
#     PROGRAM PENGOLAHAN NILAI 30 SISWA
#   ==========================================
#   Masukkan nilai siswa ke-1  : 85
#   Masukkan nilai siswa ke-2  : 90
#   ...
#   Masukkan nilai siswa ke-30 : 78
#
#   ==========================================
#         HASIL PENGOLAHAN NILAI SISWA
#   ==========================================
#     Jumlah Siswa    : 30 orang
#     Rata-rata Nilai : 82.50
#     Nilai Tertinggi : 97
#     Nilai Terendah  : 55
#   ==========================================
#
# ============================================================
#   TEKNOLOGI
# ============================================================
#
#   Bahasa  : Python 3.x
#   Library : Tidak memerlukan library eksternal (built-in only)
#
# ============================================================
