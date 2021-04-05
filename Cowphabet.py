ab = list(input())
f = list(input())
iterations = 1
index = 0
for letter in f:
    while True:
        if index==26:
            index=0
            iterations = iterations + 1
        if ab[index]==letter:
            index = index + 1
            break
        index = index + 1
print(iterations)