x,y = map(int,input().split())

name = []
for i in range(0,x):
    daftar = str(input())
    name.append(daftar)

result = []
for i in range(y):
    queue = str(input())
    if queue in name:
        result.append(name.index(queue)+1)
    else:
        result.append(-1)

print(*result,sep='\n')