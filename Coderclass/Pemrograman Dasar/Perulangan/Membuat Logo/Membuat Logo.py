n,m,l = map(int,input().split())

index = 1

for i in range(n):
    if index > l and index <= n-l:
        print(l*"*"+"."*(m-l))
        index += 1
    else:
        print('*'*m)
        index += 1