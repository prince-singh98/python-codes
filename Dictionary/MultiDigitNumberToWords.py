dict={
    0: "zero",
    1: "one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine"
}

inp = int(input("Enter your no :"))
myList = list()
rem = 0
count = 0
while inp != 0:
    myList[count] = inp % 10
    count+=1
    inp = inp // 10

for x in myList:
    print(x)



# if dict.get(inp):
#     print(dict.get(inp))
# else:
#     print("sorry try from above")