def sort(A):
    n = len(A)
    for j in range(n-1):
        for i in range(n-1-j):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]