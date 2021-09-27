num = int(input("enter a number"))

# m = num // 2

for x in range(1,num+1,1):
    if (num % x) == 0:
        print(x)
