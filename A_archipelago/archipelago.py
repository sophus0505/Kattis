import sys
import numpy as np


def dist(a, b):
    return np.sqrt((b[0] - a[0]) * 2 + (b[1] - a[1]) * 2)


def num_reach(isl, n, d):
    num_reached = []
    tol = 1 * 10 ** (-4)
    for i in range(n):
        counter = 0
        for j in range(n):
            if i == j:
                continue

            if abs(dist(isl[i], isl[j]) - d) < tol:
                counter += 1

        num_reached.append((i, counter))

    return num_reached


def sort(A, n):
    for i in range(n):
        j = i
        while j > 0 and A[j - 1][1] < A[j][1]:
            A[j], A[j - 1] = A[j - 1], A[j]
            j -= 1
    return A


n, d = input().split()
n, d = int(n), int(d)
isl = []
for i in range(n):
    x, y = input().split()
    isl.append((int(x), int(y)))

num_reached = num_reach(isl, n, d)
num_reached = sort(num_reached, n)

for n in num_reached[:-1]:
    print(n[0] + 1, end=" ")
print(num_reached[-1][0] + 1)