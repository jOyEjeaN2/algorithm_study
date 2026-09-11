N = int(input())

arr = [[0]*N for _ in range(N)]

num = 1 

if N % 2 == 0:
    for j in range(N-1, -1, -1):
        if j % 2 != 0:
            for i in range (N-1, -1, -1):
                arr[i][j] = num 
                num += 1
        else:
            for i in range(N):
                arr[i][j] = num 
                num += 1
else:
    for j in range(N-1, -1, -1):
        if j % 2 == 0:
            for i in range (N-1, -1, -1):
                arr[i][j] = num 
                num += 1
        else:
            for i in range(N):
                arr[i][j] = num 
                num += 1


for row in arr:
    print(*row)