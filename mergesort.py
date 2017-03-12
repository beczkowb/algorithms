def sort(A, p=None, r=None):
    if p is None and r is None:
        p = 0
        r = len(A) - 1

    if p < r:
        q = (p+r) // 2
        sort(A, p, q)
        sort(A, q+1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    # A=[1, 5, 10   ,   2, 5, 11]
    #    i              j
    # A=[1, 5, 10   ,   2, 5, 11]
    tmp_arr = [0 for i in range(p, r+1)]

    right_part_i = q+1
    left_part_i = p
    tmp_i = 0

    while left_part_i <= q and right_part_i <= r:
        if A[left_part_i] > A[right_part_i]:
            tmp_arr[tmp_i] = A[right_part_i]
            right_part_i += 1
        else:
            tmp_arr[tmp_i] = A[left_part_i]
            left_part_i += 1
        tmp_i += 1

    if left_part_i > q:
        tmp_arr[tmp_i:] = A[right_part_i:r+1]
    else:
        tmp_arr[tmp_i:] = A[left_part_i:q+1]

    A[p:r+1] = tmp_arr