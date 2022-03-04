"""
Program perulangan membaca buku
"""
print('Ibu menyuruh Budi untuk belajar')
print('"Budi, baca semua buku-buku kamu!"')
print('"Iya Bu"')

jumlah_buku = 10
jumlah_buku_yang_sudah_dibaca = 0

# Budi mulai membaca buku
for jumlah_buku_yang_sudah_dibaca in range(1, jumlah_buku+1):
    print(f"Buku ke {jumlah_buku_yang_sudah_dibaca} sudah dibaca")

#Budi selesai membaca buku
print(f"Budi sudah membaca semua {jumlah_buku_yang_sudah_dibaca} buku yang Budi punya")
