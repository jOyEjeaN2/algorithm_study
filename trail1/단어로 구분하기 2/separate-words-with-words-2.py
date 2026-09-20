import sys 
input = sys.stdin.readline

words = input().split()

for w in range(len(words)):
    if w % 2 == 0:
        print(words[w])