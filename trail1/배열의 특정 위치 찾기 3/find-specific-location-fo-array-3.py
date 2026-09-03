N = list(map(int, input().split()))

zero_idx = N.index(0)
sum = 0 

for i in range(zero_idx - 3, zero_idx):
    sum += N[i]

print(sum)