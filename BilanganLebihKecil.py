bilangan_A = int(input("Masukan bilangan A : "))
bilangan_B = int(input("Masukan bilangan B : "))
bilangan_C = int(input("Masukan bilangan C : "))

if bilangan_A < bilangan_B and bilangan_A < bilangan_C:
    hasil = "bilangan %i paling kecil dari %i dan %i"%(bilangan_A,bilangan_B,bilangan_C)
elif bilangan_B < bilangan_A and bilangan_B < bilangan_C:
    hasil = "bilangan %i paling kecil dari %i dan %i"%(bilangan_B,bilangan_A,bilangan_C)
elif bilangan_C < bilangan_A and bilangan_C < bilangan_B:
    hasil = "bilangan %i paling kecil dari %i dan %i"%(bilangan_C,bilangan_A,bilangan_C)
else:
    hasil = "bilangan sama"

print(hasil)