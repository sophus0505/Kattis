import sys



x, y = input().split()
x, y = int(x), int(y)


num_five = min(x, y)
x -= num_five
y -= num_five

lapper = 0
while num_five > 20:
    lapper += 1
    num_five -= 20


sum_fives = 5*num_five
sum_x = 2*x
sum_y = 3*y

while sum_x > 0:
    if sum_fives + sum_x == 100:
        lapper += 1
    sum_x -= 2

while sum_y > 0:
    if sum_fives + sum_y == 100:
        lapper += 1
    sum_y -= 3

print(lapper)
