def arrayManipulation(n, queries):
    arr = [0] * (n + 2)  # Extra size to handle b+1 easily

    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k

    max_val = 0
    current = 0
    for i in range(1, n + 1):
        current += arr[i]
        max_val = max(max_val, current)

    return max_val



print(arrayManipulation(10,[[1,5,3], [4, 8, 7], [6, 9, 1]]))