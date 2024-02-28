English = int(input("Masukan nilai : "))
MTK = int(input("Masukan nilai : "))
Indo = int(input("Masukan nilai : "))
IPA = int(input("Masukan nilai : "))
IPS = int(input("Masukan nilai : "))

ratarata1 = (English + MTK + Indo) / 3
ratarata2 = (English + MTK + Indo + IPA + IPS) / 5

if ratarata1 >= 75:
    kelulusan = "lulus"
elif ratarata2 >= 70:
    kelulusan = "lulus"
elif English > 90 and MTK > 90:
    kelulusan = "lulus"
else:
    kelulusan = "tidak lulus"

print(kelulusan)


