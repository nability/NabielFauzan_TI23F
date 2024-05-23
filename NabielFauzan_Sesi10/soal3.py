# 3.Rani memiliki sebuah list yang berisi buah-buahan. Dia ingin menghapus semua kata yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata-kata tersebut secara alfabetis. Bantulah Rani untuk mencapai ini.

# Input: kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
# Output: ['anggur', 'durian', 'jeruk', 'mangga', 'pisang']

arr1 = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
a = []

for i in arr1:
    if len(i) >= 5:
        a.append(i)

a.sort()

print(a)