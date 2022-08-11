a,b,x,y = map(int,input().split())


while True:
    if x > y:
        break
    else:
        print(x)
        x = x * a + b
