arr = ["apple", "banana", "grape", "blueberry", "orange"] 

n = input()
count = 0 

arr1 = []
    
for a in arr:
    if a[2] == n or a[3] == n:
        arr1.append(a)
        count +=1 

for row in arr1:
    print(row)

print(count)