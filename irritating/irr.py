from sys import stdin


n, k = stdin.readline().split()
t = stdin.readline().split()
c = stdin.readline().split()

handle = dict()
for i in range(int(k)):
    t_i = stdin.readline().split()
    handle[t_i[0]] = t_i[2:]


for key in handle:
    items = handle[key]
    for item in items:
        while item in t:
            print(item, end=" ")
            t.remove(item)
