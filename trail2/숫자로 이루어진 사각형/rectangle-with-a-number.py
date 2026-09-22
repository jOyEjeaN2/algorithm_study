n = int(input())

# Please write your code here.
arr = [[0]*n for _ in range(n)]
count = 1

for i in range(n):
    for j in range(n):
        if count <= 9:
            arr[i][j] = count 
            count += 1
        else:
            count = 1
            arr[i][j] = count
            count += 1


for row in arr:
    print(*row)