no1 = int(input("enter first number: "))
no2 = int(input("enter second number: "))


def sum(no1,no2):
    return no1+no2


def sub(no1,no2):
    return no1 - no2


def mul(no1,no2):
    return no1*no2


def div(no1,no2):
    return no1//no2


print(f'Addition is : {sum(no1,no2)}')
print(f'subtraction is :{sub(no1,no2)}')
print(f'Multiplication is : {mul(no1,no2)}')
print(f'Division is :{div(no1,no2)}')
