num = int(input("enter up to which number you want the series: "))

no1 = 0
no2 = 1
print(no1)
print(no2)
nextNum = no1 + no2
while nextNum < num:
    print(nextNum)
    no1 = no2
    no2 = nextNum
    nextNum = no1 + no2


