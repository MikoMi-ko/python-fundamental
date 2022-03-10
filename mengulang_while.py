"""
Mengulang sintaksis perulangan dengan while
"""

print("Budi diperintahkan oleh Ibu untuk melipat baju-bajunya")
print('"Budi, Ibu sudah selesai menjemur baju-baumu, semuanya sudah kering"')

baju = 10
baju_terlipat = 0

print(f'"Sekarang lipat semua {baju} baju-bajumu yang sudah Ibu bawa masuk!"')
print('"Iya Bu"')

# Budi mulai melipat bajunya
while baju_terlipat < baju:
    baju_terlipat = baju_terlipat + 1
    print(f"Baju ke-{baju_terlipat} sudah dilipat")

# Budi selesai melipat bajunya
print(f"Budi selesai melipat {baju_terlipat} bajunya")
