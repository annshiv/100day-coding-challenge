def binarytree(r):
    return [r,[],[]]

def insertleft(root,new_branch):
    t = root.pop(1)

    if len(t) > 1:
        root.insert(1,[new_branch,t,[]])
    else:
        root.insert(1,[new_branch,[],[]])
    return root

def insertright(root,new_branch):
    t = root.pop(2)

    if len(t) > 1:
        root.insert(2,[new_branch,[],t])
    else:
        root.insert(2,[new_branch,[],[]])
    return root

def getroot(root):
    return root[0]

def setroot(root,new_val):
    root[1] = new_val

def getleftchild(root):
    return root[1]

def getrightchild(root):
    return root[2]

if __name__ == "__main__":
    r = binarytree(3)

    insertleft(r,4)
    insertleft(r,5)
    insertright(r,6)
    insertright(r,7)
    
    print(r)