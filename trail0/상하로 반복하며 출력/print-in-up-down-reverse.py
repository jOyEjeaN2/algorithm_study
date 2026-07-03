N = int(input())

for i in range(N):
    row = []
    for j in range(N):
        if j % 2 == 0:
            row.append(i+1)
        else:
            row.append(N-i)
    print(*row, sep="")