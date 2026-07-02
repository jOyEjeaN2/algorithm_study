N = int(input())

arr = list(map(int, input().split()))

for a in range(len(arr)):
    arr[a] = arr[a]**2

print(*arr)
