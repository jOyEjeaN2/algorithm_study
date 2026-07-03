word1, word2 = input().split()

count1 = len(word1)
count2 = len(word2)

if count1 > count2:
    print(word1, count1)
elif count2 > count1:
    print(word2, count2)
elif count1 == count2:
    print("same")