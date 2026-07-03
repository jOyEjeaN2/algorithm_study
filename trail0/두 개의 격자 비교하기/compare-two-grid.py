N, M = map(int, input().split())

arr = [list(map(int, input().split())) for n in range(N)]
arr2 = [list(map(int, input().split())) for n in range(N)]
arr3 = [[0 for _ in range(M)] for _ in range(N)]

for n in range(N):
    for m in range(M):
        if arr[n][m] == arr2[n][m]:
            arr3[n][m] = 0
        else:
            arr3[n][m] = 1

for n in range(N):
    for m in range(M):
        print(arr3[n][m], end=" ")
    print()