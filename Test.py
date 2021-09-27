list = [1,2,3,4,5,2,3]

unique = dict()
# for x in range(len(list)):
#     unique[x] = list[x]
# print(unique)

for ele in list:
    if ele in unique.keys():
        unique[ele] = unique.get(ele)+1
    else:
        unique[ele] = 1
print(unique)

for ele in unique.keys():
    if unique.get(ele) ==1:
        print(ele)
