
m,n = map(int,input().split())

result = []
for x in range(1,m+1):
    baris = str(input())
    baris = baris.split()
    result.append(baris)

for x in range(0,n):
    for y in range(0,m):
        print(result[y][x],end=" ")
    print()