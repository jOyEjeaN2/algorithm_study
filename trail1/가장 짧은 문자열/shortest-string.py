a = input()
b = input() 
c = input()

max_1 = max(len(a), len(b), len(c))
min_1 = min(len(a), len(b), len(c))

result = max_1 - min_1

print(result)