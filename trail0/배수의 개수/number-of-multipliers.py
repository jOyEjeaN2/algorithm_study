arr = [int(input()) for x in range(10)]
cnt1 = 0 
cnt2 = 0

for a in arr:
    if a % 3 == 0:
        cnt1 += 1
    if a % 5 == 0:
        cnt2 += 1 


print(cnt1, cnt2)
