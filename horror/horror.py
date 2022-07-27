import sys


line1 = [int(x) for x in input().split()]
N, H, L = line1

horror_list = [int(x) for x in input().split()]

score = {}

for i in range(N):
    if i in horror_list:
        score[i] = 0
    else:
        score[i] = float("inf")



E = {x:[] for x in range(N)}
for _ in range(L):
    line = input().split()
    u = int(line[0])
    v = int(line[1])
    E[u].append(v)
    E[v].append(u)

def DFS(E, N, u):
    Q = [u]
    visited = [u]
    D = [float("inf") for _ in range(N)]
    D[u] = 0
    while Q:
        u = Q.pop()
        for v in E[u]:
            visited.append(v)
            if score[u] + 1 < D[v]:
                D[v] = score[u] + 1
                Q.append(v)
    return D
            

high_score = (0,0)
for i in horror_list:
    D = DFS(E,N,i)
    for i, d in enumerate(D):
        if d < score[i]:
            score[i] = d
        if d > high_score[1]:
            high_score = (i,d)

print(high_score)