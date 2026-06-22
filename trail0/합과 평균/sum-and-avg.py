import sys 
input = sys.stdin.readline

A,B = map(int, input().split())

total = A+B
average = total / 2

print(total, average)