arr = list(map(int, input().split()))

for a in range(8): 
    arr.append((arr[a] + arr[a+1])%10)

print(*arr, sep=" ")