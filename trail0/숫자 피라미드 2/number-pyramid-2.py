N = int(input())
num = 1

for i in range(1,N+1):
    arr = []
    for j in range(i):
        arr.append(num)
        num += 1
    print(*arr, sep=" ") 



