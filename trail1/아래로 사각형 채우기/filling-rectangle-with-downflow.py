N = int(input())

arr = [[0]*N for _ in range(N)]

for i in range(N):
    num = i+1
    for j in range(N):
        arr[i][j] = num 
        num += N
    
for row in arr:
    print(*row)