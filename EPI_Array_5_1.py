def dutch_flag(A, pivot_index):
    p = pivot_index
    part = 0
    print(A[pivot_index])  # current pivot
    for i in range(len(A)):
        print(A[p])
        if A[i] < A[p]:
            A[i], A[part] = A[part], A[i]
            if part == p:
                p = i   # update pivot to where pivot element was moved if pivot was swapped
            part += 1
    A[part], A[p] = A[p], A[part]
    print(A)


A = [1, 4, 3, 7, 2, 10, 9, 12, 45, 23, 65, 43, 100, 25, 60]
dutch_flag(A, 8)
