


def count(box, num):
    if not forest[box]:
        return 1
    for child in forest[box]:
        if child not in query:
            num += count(child, num)
    return num
        

if __name__ == '__main__':
    N = int(input())
    boxes = [int(x) for x in input().split()]
    Q = int(input())

    forest = {i:[] for i in range(1, N+1)}

    for i, box in enumerate(boxes):
        if box != 0:
            forest[box].append(i+1)

    for _ in range(Q):
        query = [int(x) for x in input().split()[1:]]
        val = 0

        for q in query:
            val += count(q, 1)

        print(val)




   
    





    
        
