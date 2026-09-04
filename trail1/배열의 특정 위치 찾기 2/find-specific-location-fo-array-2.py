arr = list(map(int, input().split()))

even_sum = 0
odd_sum = 0

for i in range(1, len(arr)+1):
    if i % 2 != 0:
        odd_sum += arr[i-1]
    elif i % 2 == 0:
        even_sum += arr[i-1]


if odd_sum > even_sum:
    result = odd_sum - even_sum
elif even_sum > odd_sum:
    result = even_sum - odd_sum 

print(result)