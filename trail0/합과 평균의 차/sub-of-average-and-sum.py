import sys 
input = sys.stdin.readline

a,b,c = map(int, input().split())
total = a+b+c
average = int(total / 3)
print(total)
print(average)
print(total - average)