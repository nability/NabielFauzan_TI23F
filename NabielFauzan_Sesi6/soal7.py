kolom = 5
baris = 4
karakter = ["A","B"]

for i in range (baris):
    for j in range (kolom):
        print(karakter[(i + j) % 2], end=" ")
    print()