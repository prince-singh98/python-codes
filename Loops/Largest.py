
# largest of 3 numbers

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if a > b:
    if a > c:
        print(f'{a} is largest')
    else:
        print(f'{c} is largest')
elif b > c:
    print(f'{b} is largest')
else:
    print(f'{c} is largest')
