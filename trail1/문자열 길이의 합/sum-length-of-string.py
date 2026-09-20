N = int(input())

words = [input() for _ in range(N)] 
count = 0
count_a = 0

for word in words:
    count += len(word)

    if word and word[0] == "a":
        count_a += 1

print(count, count_a)