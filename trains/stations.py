import sys


# h, w, n = input().split()
h, w, n = sys.stdin.readline().split()
h, w, n = int(h), int(w), int(n)

screens = [[] for _ in range(n+1)]

for i in range(n+1):
    for j in range(h):
        screens[i].append(input())

answer = screens.pop()

compares = []
min1 = h*w
min2 = h*w
for screen in screens:
    num_false = 0
    for i in range(h):
        for j in range(w):
            if screen[i][j] == '.' and answer[i][j] == 'x':
                num_false == h*w
                break
            if screen[i][j] != answer[i][j]:
                num_false = num_false + 1
    if num_false < min1:
        min2 = min1
        min1 = num_false
    elif num_false < min2:
        min2 = num_false
    compares.append(num_false)


if min1 == 0 or min2 == 0:
    print('yes')
elif min1 == h*w:
    print('no')
elif min1 < min2:
    print('yes')
else:
    print('no')

