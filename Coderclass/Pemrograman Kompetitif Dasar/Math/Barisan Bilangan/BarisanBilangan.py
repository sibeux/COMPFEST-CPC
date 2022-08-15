n,a,b = map(int,input().split())

result = 0
for x in range(1,n+1):
    if x%a == 0 or x%b == 0:
        result += 1

print(result)