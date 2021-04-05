import time


def swap(lst, start, end):
    rev = lst[start-1:end]
    rev.reverse()
    return lst[0:start-1] + rev + lst[end:]


def swap2(lst, start, end):
    depth = int((end - start + 1) / 2)
    real_start = start - 1
    real_end = end - 1
    for idx in range(depth):
        lst[real_start + idx], lst[real_end - idx] = lst[real_end - idx], lst[real_start + idx]


f = open('swap.in', 'r')
w = open('swap.out', 'w')

in_data = f.readlines()
in_data = list(map(str.strip, in_data))
in_data = [i.split(' ') for i in in_data]
iter_num = int(in_data[0][1])
a1 = int(in_data[1][0])
a2 = int(in_data[1][1])
b1 = int(in_data[2][0])
b2 = int(in_data[2][1])
stt_time = time.time()
arr = [i for i in range(1, int(in_data[0][0])+1)]
ref = [i for i in range(1, int(in_data[0][0])+1)]
end_time = time.time()
print(" arr time : {:.6f}".format(end_time - stt_time))
count = 1
while True:
    arr = swap(arr, a1, a2)
    arr = swap(arr, b1, b2)
    if arr == ref:
        break
    count += 1
    # swap2(arr, a1, a2)
    # swap2(arr, b1, b2)
depth = iter_num%count
for k in range(depth):
    arr = swap(arr, a1, a2)
    arr = swap(arr, b1, b2)
for i in arr:
    w.write(str(i)+'\n')