n,q = map(int,input().split())

word = str(input())
word = [i for i in word]
for x in range(q):
    x,a,b = map(int,input().split())
    if x == 2:
        wordReverse = word[a-1:b]
        wordReverse.reverse()
        word = word[:a-1]+wordReverse
    elif x == 1:
        word[a-1],word[b-1] = word[b-1],word[a-1]

print(*word,sep="")