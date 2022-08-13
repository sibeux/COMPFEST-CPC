n,m = map(int,input().split())
value = []
for i in range(1,n+1):
    value.append(i)
pop = str(input())
pop = pop.split()

for i in pop:
    value.remove(int(i))

print(value, end=" ")