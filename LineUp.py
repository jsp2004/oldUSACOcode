def permutation(lst):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i + 1:]
        for p in permutation(remLst):
            l.append([m] + p)
    return l

f = open('lineup.in', 'r')
w = open('lineup.out', 'w')
input = f.readlines()
input = list(map(str.strip, input))
check = []
for i in range(1,int(input[0])+1):
    check.append(input[i].split(' must be milked beside '))
cows = ['Beatrice','Belinda','Bella','Bessie','Betsy', 'Blue', 'Buttercup', 'Sue']
totalcombs = permutation(cows)
ind = 0
for comb in totalcombs:
    conditions = 0
    for s in check:
        ind = comb.index(s[0])
        if ind == 0:
            if comb[ind+1]==s[1]:
                conditions += 1
        elif ind == 7:
            if comb[ind-1]==s[1]:
                conditions += 1
        elif (comb[ind-1]==s[1]) or (comb[ind+1]==s[1]):
            conditions += 1
        else:
            break
    if conditions == int(input[0]):
        for cow in comb:
            w.write(cow+'\n')
        break
