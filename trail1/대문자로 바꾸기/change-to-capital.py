arr = [[x.upper() for x in input().split()] for _ in range(5)]

for row in arr:
    print(*row)