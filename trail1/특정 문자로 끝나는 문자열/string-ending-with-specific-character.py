import sys 
input = sys.stdin.readline

words = [input().strip() for _ in range(10)]
a = input().strip()
found = False


for word in words:
    if word[-1] == a:
        print(word)
        found = True

if not found:
    print("None")