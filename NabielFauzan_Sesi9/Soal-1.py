# 1.Ilham memiliki sebuah list yang berisi angka-angka acak. Anda ingin menghapus semua angka yang memiliki nilai kurang dari 5 dan menggantinya dengan nilai 0, dan akan mengurutkan dari nilai yang terbesar ke yang terkecil. Bantu Ilham untuk menyelesaikan persoalan tersebut menggunakan array method.

# Input: [8, 3, 12, 4, 7, 2]
# Output: [12, 8, 7, 0, 0, 0]

arr1 = [8, 3, 12, 4, 7, 2]
arr1.sort(reverse=True)

for i in range (len(arr1)):
    if arr1[i] <5 :
        arr1[i] = 0

print(arr1)