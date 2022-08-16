n = int(input())

value = 0
for x in range(1,n+1):
    for y in range(1,x+1):
        if x%y == 0:
            value += 1

print(value)