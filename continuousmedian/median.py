

def insertion(A, val, n):
    print(A)
    if not A:
        return A.append(val)
    if val > A[n-1]:
        return A.append(val)
    elif val < A[0]:
        return A.insert(0, val)
    left = 0
    right = n
    middle = n // 2
    while left < right:
        if A[middle] < val:
            left = middle
            middle = middle + (right - left) // 2

        elif A[middle] > val:
            right = middle 
            middle = middle - (right - left) // 2
    A.insert(middle, val)
    return A






cases = int(input())

for _ in range(cases):
    N = int(input())
    A = [int(x) for x in input().split()]
    B = []
    for i, val in enumerate(A):
        C = insertion(B, val, i)
        print(C)
        