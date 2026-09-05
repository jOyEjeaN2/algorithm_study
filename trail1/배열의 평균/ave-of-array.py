arr = [list(map(int, input().split())) for _ in range(2)]

row = len(arr)
col = len(arr[0])

row_avgs = []
for i in range(row):
    row_sum = 0 
    for j in range(col):
        row_sum += arr[i][j] 
    row_avgs.append(row_sum / col)

col_avgs = []
for j in range(col):
    col_sum = 0
    for i in range(row):
        col_sum += arr[i][j] 
    col_avgs.append(col_sum / row)

total_sum = 0 
for i in range(row):
    for j in range(col):
        total_sum += arr[i][j]
total_avg = total_sum / (row * col)
    



print(*(f'{avg:.1f}' for avg in row_avgs))
print(*(f'{avg:.1f}' for avg in col_avgs))
print(f'{total_avg:.1f}')