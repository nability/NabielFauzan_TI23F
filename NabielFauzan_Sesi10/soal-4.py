# 4.Dewi memiliki dua list yang berisi nama-nama buah-buahan. Dia ingin menggabungkan kedua list tersebut dan menghapus semua buah yang memiliki nama yang sama. Setelah itu, dia ingin mengurutkan sisa buah-buahan secara alfabetis. Bantu Dewi

# Input: ["apel", "jeruk", "mangga"], ["apel", "anggur", "nanas"]
# Output: ['anggur', 'apel', 'jeruk', 'mangga', 'nanas']

arr1= ["apel", "jeruk", "mangga"]
arr2 = ["apel", "anggur", "nanas"]

buah = arr1.copy()
buah.extend(arr1)
buah_2 = set(buah)
buah_Dewi = sorted(buah_2)

print(buah_Dewi)