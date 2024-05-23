# 5.Dina memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus semua nilai yang kurang dari 10 dan lebih dari 100, dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar. Implementasikan ini dengan menggunakan metode-metode yang tepat dari list.

# Input: [105, 20, 8, 150, 30, 5, 200]
# Output: [20, 30]

arr1 = [105, 20, 8, 150, 30, 5, 200]
arr1.sort()

for i in range (len(arr1)):
    if arr1[i] < 10:
        arr1[i] = 0
    elif arr1[i] > 100:
        arr1[i] = 0

while 0 in arr1:
    arr1.remove(0)

print(arr1)