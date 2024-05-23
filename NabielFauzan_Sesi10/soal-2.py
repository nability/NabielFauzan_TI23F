# 2.Budi memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus semua nilai yang merupakan bilangan ganjil dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar. Bantu budi untuk menyelesaikan persoalan tersebut menggunakan array method.

# Input: [7, 4, 9, 2, 5, 1]
# Output: [2, 4]

arr1 = [7, 4, 9, 2, 5, 1]
arr1.sort()

for i  in range (len(arr1)):
    if arr1[i] % 2 != 0:
        arr1[i] = 0

while 0 in arr1:
    arr1.remove(0)

print(arr1)