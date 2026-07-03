N = int(input())

arr = list(map(int, input().split()))
arr2 = []

for a in arr:
    if a % 2 == 0:
        arr2.append(a)

arr2.reverse()
print(*arr2)