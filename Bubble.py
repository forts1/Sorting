def bubble(A):
    for i in range (0, len(A)):
        for j in range (0,len(A)-1):
            if A[j+1]< A[j]:
                A[j+1],A[j]= A[j],A[j+1]
            else:
                pass
    return f"The sorted array is {A}"
bubble([1111,11,1])
    
