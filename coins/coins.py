import sys

def make_choice(n):
    k = n%4
    if k == 0:
        k = 3
    elif k == 2:
        k = 1
    elif k == 3:
        k = 2
    elif k == 0:
        k = 3
    return k

def make_him_suffer(n):
    print(n-1)
    print('I give up')

n = int(input())

while n > 4:
    k = make_choice(n)
    n -= k
    print(k, flush=True)
    k = int(input())
    n -= k

make_him_suffer(n)

exit()



