import sys 
input = sys.stdin.readline

n, m = map(int, input().split())

# Please write your code here.

def rectangle(n,m):
    arr = [[1] * m for _ in range(n)]
    for row in arr:
        print("".join(map(str, row)))

rectangle(n,m)