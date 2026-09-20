import sys 
input = sys.stdin.readline

words = input().split()

for w in range(len(words)-1, -1, -1):
    print(words[w])