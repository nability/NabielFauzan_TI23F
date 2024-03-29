baris = 6
kolom = 7

for i in range(1, baris):
    for j in range(i, kolom - 1):
        print(j, end=" ")
    print()