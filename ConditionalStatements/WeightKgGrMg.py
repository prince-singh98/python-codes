weight = int(input("enter weight in kg: "))

print("do you want in gram or milligram")
print("press 1 for gram")
print("press 2 for milligram")
ch=int(input("enter your choice"))

if(ch==1):
    gram = 1000 * weight
    print("weight in gram is : ", gram)
elif(ch==2):
    milli = 1000000 * weight
    print("weight in milli gram is : ", milli)
else:
    print("Try one from above")

