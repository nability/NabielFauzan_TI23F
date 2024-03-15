temp = input("Masukan jenis suhu yang ingin di konversikan (celcius / fahrenheit): ")
suhu = float(input("Masukan derajat suhunya : "))

if temp == "celcius":
    fahrenheit = (9/5* suhu) + 32
    print(f"hasil konversi dari suhu celcius {suhu} derajat menjadi fahrenheit {fahrenheit} derajat")
else:
    celcius = 5/9 * (suhu - 32)
    print(f"hasil konversi dari suhu celcius {suhu} derajat menjadi fahrenheit {celcius} derajat")
