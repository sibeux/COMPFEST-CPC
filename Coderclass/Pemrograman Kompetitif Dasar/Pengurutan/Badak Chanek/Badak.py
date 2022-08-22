from unittest import result


n,q = map(int,input().split())

cula = sorted(map(int,input().split()))

result = []
for i in range(q):
    result.append(cula[int(input())-1])

print(*result,end="\n")