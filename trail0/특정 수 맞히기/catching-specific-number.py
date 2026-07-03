while True:
    N = int(input())
    if N < 25:
        print("Higher")
    elif N > 25:
        print("Lower")
    elif N == 25:
        print("Good")
        break