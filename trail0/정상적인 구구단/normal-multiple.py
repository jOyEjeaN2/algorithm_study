N = int(input())

for n in range(1,N+1):
    for j in range(1,N+1):
        if j < N:
            print(f"{n} * {j} = {n*j}", end=", ")
        else:
            print(f"{n} * {j} = {n*j}", end="")
    print()