n = int(input())
heights = list(map(int, input().split(" ")))
heights.sort()
heights.reverse()
limits = list(map(int, input().split(" ")))
poss = 1
count = 0
index = 0
for h in heights:
    for lim in limits:
        if lim >= h:
            count = count + 1
    poss = poss * (count-index)
    count = 0
    index = index + 1
print(poss)