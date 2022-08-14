def palindrome(kata):
    if kata == kata[::-1]:
        return "palindrom"
    else:
        return "bukan palindrom"

n = int(input())

result = []
for x in range(n):
    result.append(palindrome(input()))

print(*result, sep="\n")