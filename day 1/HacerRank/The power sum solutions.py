x = int(input().strip())
n = int(input().strip())

max_num = int(x**(1/n))

powers = [num**n for num in range(1,max_num+1)]

def power_sum(x, powers):
    running_total = 0
    for ind, num in enumerate(powers):
        if x - num == 0:
            running_total += 1
        elif x - num < 0:
            pass
        else:
            running_total += power_sum(x - num, powers[ind + 1:])
    return running_total
            
            
print(power_sum(x, powers))