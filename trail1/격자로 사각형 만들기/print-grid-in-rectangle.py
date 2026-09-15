N = int(input())

arr = [[0]*N for _ in range(N)]

for i in range(1):
    for j in range(N):
        arr[i][j] = 1

for i in range(N):
    for j in range(1):
        arr[i][j] = 1 

for i in range(1,N):
    for j in range(1,N):
        arr[i][j] = arr[i-1][j] + arr[i][j-1] + arr[i-1][j-1]

for row in arr:
    print(*row)