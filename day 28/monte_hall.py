import random

doors = [0]*3
goat_doors = [0]*2
swap = 0
dont_swap = 0
x = random.randint(0,2)
doors[x] = 'BMW'
count = 0
while(count < 10):
    for i in range(0,3):
        if i == x:
            continue
        else:
            doors[i] = 'Goat'
            goat_doors.append(i)
    choice = int(input("Enter your choice "))
    door_open = random.choice(goat_doors)
    while(door_open==choice):
        door_open = random.choice(goat_doors)
    ch = input("are want to swap y/n ")
    if ch == 'y':
        if(doors[choice]=='Goat'):
            print("player won")
            swap += 1
        else:
            print("Player lost")
    else:
        if(doors[choice] == 'Goat'):
            print("Player lost")
        else:
            print("Player won")
            dont_swap += 1
    count += 1

print(swap)
print(dont_swap)