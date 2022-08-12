x,y = map(int,input().split())
found = str(input().split())

for x in range(1,x+1):
    if str(x) in found:
        continue
    else:
        print(x,end=" ")
