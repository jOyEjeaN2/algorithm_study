import sys 
input = sys.stdin.readline 

N = int(input())

words = [input().strip() for _ in range(N)]
target = input().strip()
total_len = 0 
count = 0

for word in words:
    if word[0] == target:
        count += 1
        total_len += len(word)

    
result = total_len / count
print(f"{count} {result:.2f}")