from unittest import result


a,b,c,x = map(int,input().split())

x_awal = x
result = 0
while True:
    x = (a*x+b)%c
    result += 1
    if x == x_awal:
        break

print(result)