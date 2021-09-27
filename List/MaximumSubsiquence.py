list = [1, 2, 3, 7, 7, 9, 9, 9, 8, 8, 8, 8, 8]

count = 1
max = 1

for x in range(len(list)-1):
    if (list[x] == list[x+1]):
        count = count + 1
        if max<count:
            max = count
    else:
        count=1

print(max)
