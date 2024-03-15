bilangan = int(input("Masukan bilangan : "))

if bilangan %2==0 and bilangan >0:
    hasil = f"{bilangan} adalah bilangan genap dan positif"
elif bilangan %2==0 and bilangan <0:
    hasil = f"{bilangan} adalah bilangan genap dan negatif"
elif bilangan %2!=0 and bilangan <0:
    hasil = f"{bilangan} adalah bilangan ganjil dan negatif"
elif bilangan %2!=0 and bilangan >0:
    hasil = f"{bilangan} adalah bilangan ganjil dan positif"
else:
    hasil = f"{bilangan} adalah bilangan netral"

print(hasil)
