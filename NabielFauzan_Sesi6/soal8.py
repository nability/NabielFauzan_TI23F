baris = 5
karakter = ["S","O"]

for i in range (baris):
    for j in range (baris - i):
        print(karakter[(i + j) % 2], end=" ")
    print( )