# Tugas 1 course Udemy

print('"Budi, belikan ibu sebotol susu, kalo mereka punya telor beli 6 ya"')
print('"Oke Ibu"')

jumlah_susu = 3
jumlah_telur = 1
print(f"Toko mempunyai {jumlah_telur} butir telur")
print(f"Toko mempunyai {jumlah_susu} botol susu")

if jumlah_susu > 0:
    print("Budi mengecek jumlah uang dan cukup untuk berbelanja")
    if jumlah_telur >= 1 and jumlah_susu >= 6:
        print("Budi membeli 6 botol susu")
        print("Budi selesai berbelanja dan pulang ke rumah")
    else:
        print("Budi membeli 1 botol susu")
        print("Budi selesai berbelanja dan pulang ke rumah")
else:
    print("Ternyata toko tidak mempunyai susu")
    print("Budi pulang ke rumah")

if jumlah_susu == 0:
    print('"Susunya kosong bu"')
    print('"Ohh yasudah, terimakasih Budi"')
else:
    if jumlah_telur == 0:
        print('"Terimakasih Budi')
        print('"Sama-sama bu"')
    else:
        if jumlah_susu < 6:
            print('"Terimakasih Budi')
            print('"Sama-sama bu"')
        else:
            print('"Lhoh ko beli 6 susunya? Ibu kan minta cuma 1 saja"')
            print('"Karena mereka punya telor bu"')

