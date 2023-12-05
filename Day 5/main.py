with open("Day 5\input.txt") as f:
    data=f.read().split("\n")

# data = open("Day 05/data.txt", "r").read().split("\n")

seeds = [int(n) for n in data[0].split(":")[1].split()]
maps = [[tuple(int(n) for n in i.split()) for i in d.strip().split("\n")[1:]] for d in "\n".join(data[2:]).split("\n\n")]

for mapx in maps:
    for i, val in enumerate(seeds):
        for (destStart, srcStart, rangeLen) in mapx:
            if val >= srcStart and val < (srcStart + rangeLen):
                seeds[i] = destStart + (val - srcStart)
                break

print("Problem 9:", min(seeds))

seeds = [int(n) for n in data[0].split(":")[1].strip().split()]
valRanges = list(zip(seeds[0::2], seeds[1::2]))

for mapx in maps:
    for i, (valStart, valRange) in enumerate(valRanges):
        for (destStart, srcStart, rangeLen) in mapx:
            srcEnd = srcStart + rangeLen - 1
            if valStart >= srcStart and valStart <= srcEnd:
                valEnd = valStart + valRange - 1
                mappedStart = destStart + (valStart - srcStart)
                if valEnd <= srcEnd:
                    valRanges[i] = (mappedStart, valRange)
                else:
                    valRanges[i] = (mappedStart, srcEnd - valStart + 1)
                    valRanges.append((srcEnd + 1, valRange - srcEnd + valStart - 1))
                break

print("Problem 10:", min(v[0] for v in valRanges))