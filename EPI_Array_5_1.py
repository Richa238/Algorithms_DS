def dutch_flag(A, pivot_index):
    p=pivot_index
    part=0
    print(A[p])
    for i in range(len(A)):
        if A[i]<A[p]:
            A[part],A[i]=A[i],A[part]
            part+=1
    A[part],A[p]=A[p],A[part]
    print(A)
A = [1, 4, 3, 7, 2, 10, 9, 12, 45, 23, 65, 43, 100, 25, 60]
#    0  1  2  3  4  5   6  7  8    9   10  11  12   13  14
dutch_flag(A,8)
