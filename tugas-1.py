# Tugas 1 course Udemy

print('"Budi, belikan ibu sebotol susu, kalo mereka punya telor beli 6 ya"')
print('"Oke Ibu"')

# Sampai di toko
susu = True
telor = True
if susu:
    print('Budi membeli 1 susu')
    if telor:
        print('Budi melihat ada telor')
        print('Budi membeli 5 susu lagi')
else:
    print('Budi tidak membeli susu karena susu tidak ada')

print('Budi pulang ke rumah')
print('"Ini belanjaannya bu"')

# Respon ibu
if susu:
    print('"Oke terimakasih Budi"')
    if telor:
        print('"Lhoh kog beli 6 susu?"')
        print('"Karena mereka punya telor bu"')
else:
    print('"Coba ke toko lain Budi"')
