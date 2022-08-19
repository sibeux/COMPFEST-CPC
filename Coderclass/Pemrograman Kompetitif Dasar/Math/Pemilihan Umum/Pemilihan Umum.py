x,y = map(int,input().split())

def fpb(a, b):
    if(b == 0):
        return abs(a)
    else:
        return fpb(b, a % b)

print(x*y//fpb(x,y))