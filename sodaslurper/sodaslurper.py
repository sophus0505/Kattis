import sys




def sodas_consumed(bottles, found_bottles, num_bottles):
    sodas_consumed = 0

    while bottles >= num_bottles:
        bottles -= num_bottles - 1
        sodas_consumed += 1


    bottles += found_bottles 


    while bottles >= num_bottles:
            bottles -= num_bottles - 1
            sodas_consumed += 1
    return sodas_consumed

if __name__ == '__main__':

    bottles, found_bottles, num_bottles = sys.stdin.readline().split()
    bottles = int(bottles)
    found_bottles = int(found_bottles)
    num_bottles = int(num_bottles)
    sodas_consumed = sodas_consumed(bottles, found_bottles, num_bottles)
    print(sodas_consumed)
    


