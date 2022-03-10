"""
Program perulangan membaca buku dengan while
"""
print("Ibu menyuruh Budi untuk belajar")
print('"Budi, baca semua buku-buku kamu sampai paham!"')
print('"Iya Bu"')

jumlah_buku = 10
sudah_dibaca = 0
jumlah_paham = 0

# Budi mulai membaca buku
print(f"Jumlah buku yang sudh dibaca dan dipahami {jumlah_paham}")

while sudah_dibaca < jumlah_buku * 2:
    sudah_dibaca = sudah_dibaca + 1
    if jumlah_paham == jumlah_buku - 1:
        print(f"Buku ke {jumlah_paham + 1} belum paham")
    else:
        jumlah_paham = jumlah_paham + 1
        print(f"Buku ke {jumlah_paham} sudah dibaca dan paham")

print(f"Jumlah buku yang sudah dipahami {jumlah_paham}")
if jumlah_paham == jumlah_buku:
    print('"Bu semua buku sudah dibaca dan dipahami"')
else:
    print(f'"Budi hanya memahami {jumlah_paham} buku"')
