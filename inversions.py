def count_inversions(A, p=None, r=None):
    if p is None and r is None:
        p = 0
        r = len(A) - 1

    if p < r:
        q = (p+r) // 2
        inversions = 0
        inversions += count_inversions(A, p, q)
        inversions += count_inversions(A, q+1, r)
        inversions += merge(A, p, q, r)
        return inversions
    else:
        return 0


# 2 3 8 6 1
def merge(A, p, q, r):
    L = A[p:q+1]
    R = A[q+1:r+1]
    inversions = 0
    i = p
    lj, rj = 0, 0
    while i <= r and lj < len(L) and rj < len(R):
        if L[lj] > R[rj]:
            A[i] = L[lj]
            inversions += len(R) - rj
            lj += 1
        else:
            A[i] = R[rj]
            rj += 1
        i += 1
    if lj > len(L) - 1:
        A[i:r+1] = R[rj:]
    else:
        A[i:r+1] = L[lj:]

    return inversions