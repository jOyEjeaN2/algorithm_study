# Please write your code here.
def print_number_square(n):
    arr = [[0]*n for _ in range(n)]
    num = 1

    for i in range(n):
        for j in range(n):
            if num <= 9:
                arr[i][j] = num
                num += 1
            else:
                num = 1
                arr[i][j] = num
                num += 1

    for row in arr:
        print(*row)

n = int(input())
print_number_square(n)