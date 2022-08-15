n,m = map(int,input().split())


def banyakJalan(x=1,y=1,result=0):
    if x==n and y==m:
        return result+1
    if x<n:
        result = banyakJalan(x+1,y,result)
    if y<m:
        result = banyakJalan(x,y+1,result)
    return result

print(banyakJalan())