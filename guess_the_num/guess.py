import sys

true_num = 43

num = int(input("Enter a number between 1 and 1000: "))

left = 1
right = 1000

while left < right:
    num = int(input())
    if num == true_num:
        print("correct", flush=True)
        exit()
    elif num < true_num:
        left = num
        print("higher", flush=True)
    else:
        right = num
        print("lower", flush=True)
        

    