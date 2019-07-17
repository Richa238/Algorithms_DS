

#Without using additional space distribute numbers in an array so that even numbers are at teh start and odd numbers are after that
#used partitioning, partitioned data into even, odd and unclassified


def even_odd_array(A):
    even_index=0
    odd_index=len(A)-1

    while even_index<odd_index:
        if A[even_index]%2==0:
            even_index+=1 #incrementing even index if even number found

        else:
            A[even_index],A[odd_index]=A[odd_index],A[even_index]
            odd_index-=1
    print(A)


A=[1,4,3,7,2,10]
even_odd_array(A)