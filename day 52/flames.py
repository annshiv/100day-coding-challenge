# import packages
import string

# take two name as input
l1 = list(map(str,input("Enter your First name : ").lower().strip()))
l2 = list(map(str,input("Enter your Second name : ").lower().strip()))

# remove space
try:
    l1.remove(" ")
    l2.remove(" ")
except:
    ValueError

# remove matching letter
def remove_matching_letter(l1,l2):
    for i in range(len(l1)):
        for j in range(len(l2)):
            if l1[i] == l2[j]:
                c = l1[i]
                l1.remove(c)
                l2.remove(c)
                l = l1 + ['*'] + l2
                return [l,True]
    l = l1 + ['*'] + l2
    return [l,False]

proceed = True
while proceed:
    ret_list = remove_matching_letter(l1,l2)
    con_list = ret_list[0]
    proceed = con_list[1]
    star_ind = con_list.index('*')
    l1 = con_list[:star_ind]
    l2 = con_list[star_ind+1:]
    break

count = len(l1)+len(l2)
result = ['Friend','Love','Affection','Marriage','Enemy','Sibilings']

while len(result)>1:
    split_index = (count%len(result)) - 1
    if split_index >= 0:
        right = result[split_index+1:]
        left = result[:split_index]
        result = right + left
    else:
        result = result[:len(result)-1]

print(result[0])