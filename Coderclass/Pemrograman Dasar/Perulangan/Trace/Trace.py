n = int(input())

output = 0
for i in range(0,n):
    value = str(input())
    value = value.split()
    output += int(value[i])

print(output)