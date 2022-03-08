"""
Program perulangan membaca buku dengan while
"""
print("Ibu menyuruh Budi untuk belajar")
print('"Budi, baca semua buku-buku kamu!"')
print('"Iya Bu"')

jumlah_buku = 1000
jumlah_buku_yang_sudah_dibaca = 0

# Budi mulai membaca buku
while jumlah_buku_yang_sudah_dibaca < jumlah_buku:
    jumlah_buku_yang_sudah_dibaca = jumlah_buku_yang_sudah_dibaca + 1
    print(f"Budi membaca buku ke-{jumlah_buku_yang_sudah_dibaca}")

print(f"Budi sudah membaca {jumlah_buku_yang_sudah_dibaca} buku")
