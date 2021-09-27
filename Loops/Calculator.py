firstNum = int(input("enter first number: "))
secondNum = int(input("enter second number: "))

print("choose the operation you want to perform")
print("press + for addition")
print("press - for subtraction")
print("press * for multiplication")
print("press / for division")
ch = input("enter your choice: ")

if ch == '+':
    print(f'{firstNum} + {secondNum} = {firstNum + secondNum}')
elif ch == '-':
    print(f'{firstNum} - {secondNum} = {firstNum - secondNum}')
elif ch == '*':
    print(f'{firstNum} * {secondNum} = {firstNum * secondNum}')
elif ch == '/':
    print(f'{firstNum} / {secondNum} = {firstNum / secondNum}')
else:
    print("Try one from above choice :)")
