n = int(input())

value = []
for x in range(1, n+1):
    value.append(int(input()))

value = value[::-1]
for x in value:
    print(x)