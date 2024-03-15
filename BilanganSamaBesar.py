bilangan_A = int(input("Masukan bilangan A : "))
bilangan_B = int(input("Masukan bilangan B : "))
bilangan_C = int(input("Masukan bilangan C : "))

if bilangan_A > bilangan_B and bilangan_A > bilangan_C:
    hasil = (f"bilangan {bilangan_A} lebih besar dari bilangan {bilangan_B} dan {bilangan_C}")
elif bilangan_B > bilangan_A and bilangan_B > bilangan_C:
    hasil = (f"bilangan {bilangan_B} lebih besar dari bilangan {bilangan_A} dan {bilangan_C}")
elif bilangan_C > bilangan_A and bilangan_C > bilangan_B:
    hasil = (f"bilangan {bilangan_C} lebih besar dari bilangan {bilangan_A} dan {bilangan_B}")
elif bilangan_A == bilangan_B and bilangan_A > bilangan_C:
    hasil = (f"bilangan {bilangan_A} sama besar dengan {bilangan_B} dan lebih dari bilangan {bilangan_C}")
elif bilangan_B == bilangan_C and bilangan_B > bilangan_A:
    hasil = (f"bilangan {bilangan_B} sama besar dengan {bilangan_C} dan lebih dari bilangan {bilangan_A}")
elif bilangan_C == bilangan_A and bilangan_C > bilangan_B:
    hasil = (f"bilangan {bilangan_C} sama besar dengan {bilangan_A} dan lebih dari bilangan {bilangan_B}")
else:
    hasil = "bilangan sama"

print(hasil)