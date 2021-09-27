
str = "eduTech"
list = list(str)
print(list)
dictan = {

}
for x in range(len(list)):
    dictan.key = list[x]
    dictan.value = 1

print(dictan)

# solution

str="samuelMisra"
elements=list(str)
unique=dict()


# solution 2
for ele in elements:
    unique[ele]=ele

for ele in elements:
    if(ele in unique.keys()):
        unique[ele]=unique.get(ele)+1
    else:
        unique[ele]=1

print(unique)
