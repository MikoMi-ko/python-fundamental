"""
Sintaksiss perulangan dengan for (mengulang)
"""

print("Budi terlambat sampai ke sekolah, sehingga didisiplinkan oleh BK")
print('"Budi kamu kenapa bisa terlambat ke sekolah?"')
print('"Saya bangun kesiangan Pak"')
print('"Yasudah besok lagi jangan bangan kesiangan lagi, kamu sekarang lakukan push-up"')

push_up = 10
finished_set = 0

# Guru BK memerintahkan Budi untuk push-up
print(f'"Sekarang kamu lakukan push-up sebanyak {push_up} kali!"')
print('"Siap Pak!"')

for finished_set in range(1, push_up + 1):
    print(f"Budi push-up ke {finished_set}")

# Budi selesai push-up
print(f"Budi sudah push-up sebanyak {finished_set} kali")

print('"Kamu boleh kembali ke kelas Budi"')
print('"Baik Pak, terimakasih"')
