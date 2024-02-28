kilogram = int(input("berapa kilogram yang mau dibeli : "))

if kilogram <= 2:
    harga : 20000
elif kilogram <= 5:
    harga = 18000
elif kilogram >= 5:
    harga = 16000
totalHarga = kilogram * harga

print("harga yang harus dibayar jika membeli %i mangga adalah %i"%(kilogram, totalHarga))