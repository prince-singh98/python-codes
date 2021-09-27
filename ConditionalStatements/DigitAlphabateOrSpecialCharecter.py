char = input("enter a alphabet")
if((char>='a' and char<='z') or (char>='A' and char<='Z')):
    print(char,"is alphabet")
elif(char>='0' and char<='9'):
    print(char, "is digit")
else:
    print(char, "is special character")

