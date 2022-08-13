n = int(input())

harga = str(input())
harga = harga.split()

# 3 2 4 1
for i in range(n):
    for j in range(i+1,n):
        if harga[i] > harga[j]:
            harga[i],harga[j] = harga[j],harga[i]
            print(i+1,j+1)