with open("Day 19\input.txt") as f:
    s=f.read().strip()
left, right = s.split("\n\n")


d = []
for l in left.split("\n"):
    mid = l.index("{")
    name = l[:mid]
    d.append([])
    d[-1].append(name)
    # print(name)
    for cons in l[mid+1:-1].split(","):
        # print(cons)
        if ":" in cons:
            ll, rr = cons.split(":")
            d[-1].append((ll,rr))
        else:
            d[-1].append((None, cons))

ans = 0
for r in right.split("\n"):
    dic = {}
    for pair in r[1:-1].split(","):
        # print(pair)
        VN, VR = pair.split("=")
        dic[VN] = int(VR)
    current = "in"
    while current not in ["R","A"]:
        for cons in d:
            if cons[0] == current:
                for para in cons[1:]:
                    pl, pr = para
                    if pl == None:
                        current = pr
                        print(r, current)
                        break
                    else:
                        if (pl[1] == ">" and dic[pl[0]] > int(pl[2:])) or (pl[1] == "<" and dic[pl[0]] < int(pl[2:])):
                            current = pr
                            # print(r, current)
                            break
        if current == "A":
            for k in dic:
                ans += dic[k]
    
print(ans)
        
def total(ins, ranges):
    ans = 0
    if ins == "R":
        return 0
    if ins == "A":
        ans = 1
        for a in ranges:
            ans *= len(a)
        return ans
    entry = None
    for k in d:
        if k[0] == ins:
            entry = k[1:]

    for cons in entry:
        l, r = cons
        if l == None:
            ans += total(r, ranges)
        else:
            new_ranges = [[j for j in i] for i in ranges]
            index = "xmas".index(l[0])
            lamb = None
            if l[1] == ">":
                lamb = lambda x: x>int(l[2:])
            else:
                lamb = lambda x: x < int(l[2:])
            new_ranges[index] = list(filter(lamb, new_ranges[index]))
            ranges[index] = list(filter(lambda x: not lamb(x), ranges[index]))
            ans += total(r, new_ranges)
    return ans

print(total("in", [[i for i in range(1, 4001)] for j in range(4)]))


# number 60 globally!!!! I made it!!!!!!