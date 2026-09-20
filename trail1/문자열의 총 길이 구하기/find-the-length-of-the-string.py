import sys 

words = sys.stdin.read().split()

count = 0 

for word in words:
    count += len(word)

print(count)