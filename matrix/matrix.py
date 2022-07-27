import sys 

def inverse(a, b, c, d):
    det = a*d - b*c
    cock = a
    a = d
    d = cock
    b = -b
    c = -c
    print(f"{int(a/det)} {int(b/det)}")
    print(f"{int(c/det)} {int(d/det)}")

for i in range(1, 6):
    try:
        a, b = input().split()
        c, d = input().split()
        a, b, c, d = int(a), int(b), int(c), int(d)
        
        print(f"Case: {i}")
        inverse(a, b, c, d)
        input()
    except EOFError:
        break 

