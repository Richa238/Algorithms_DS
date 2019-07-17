def dutch_flag(A, pivot_index):
    p=pivot_index
    part=0
    for i in range(len(A)):
        if A[i]<A[p]:
            A[i],A[part]==A[part],A[i]
            part+=1
        elif A[i]==A[p]:
            continue
        elif A[i]>A[p]:
            continue
    A[part],A[p]==A[p],A[part]
    print(A)

A = [1, 4, 3, 7, 2, 10, 9, 12, 45, 23, 65, 43, 100, 25, 60]
dutch_flag(A,8)
