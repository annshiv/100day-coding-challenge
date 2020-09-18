def solve(s):
    res = []
    l = s.split(" ")
    for i in l:
        res.append(i.capitalize())
    return " ".join(res)