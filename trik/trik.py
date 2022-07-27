import sys 

def borko(line):
    cup = [True, False, False]
    for move in line:
        if move == "A":
            a = cup[0]
            cup[0] = cup[1]
            cup[1] = a 
        elif move == "B":
            a = cup[2]
            cup[2] = cup[1]
            cup[1] = a 
        else:
            a = cup[2]
            cup[2] = cup[0]
            cup[0] = a 
    if cup[0]:
        return 1
    elif cup[1]:
        return 2
    else:
        return 3
    



def main():
    line = input()
    ball = borko(line)
    print(ball)

main()