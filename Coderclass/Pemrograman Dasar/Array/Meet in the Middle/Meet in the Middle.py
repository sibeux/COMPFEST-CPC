n = input()

n = str(input())
value = n.split()

def hasil(value,x=0,y=-1,index=len(value),result=[]):
    if index == 1:
        result.append(value[x])
        print(" ".join(result))
    elif index == 0:
        print(" ".join(result))
    else:
        result.append(value[x])
        result.append(value[y])
        hasil(value,x+1,y-1,index-2)

hasil(value)