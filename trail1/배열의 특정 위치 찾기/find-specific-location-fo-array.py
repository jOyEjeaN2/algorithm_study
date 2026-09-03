A = list(map(int, input().split()))

sum1 = 0
sum2 = 0
cnt = 0

for i in range(1, len(A)+1):
    if i % 2 == 0:
        sum1 += A[i-1] 
    if i % 3 == 0:
        sum2 += A[i-1] 
        cnt += 1
    
avg = sum2 / cnt 
print(sum1, f"{avg:.1f}")
    
