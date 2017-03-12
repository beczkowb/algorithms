def sort(A):
    for j in range(0, len(A)-1):
        min_i = j
        for i in range(j+1, len(A)):
            if A[i] < A[min_i]:
                min_i = i

        A[min_i], A[j] = A[j], A[min_i]