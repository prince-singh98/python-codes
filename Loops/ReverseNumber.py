number = int(input("enter a number: "))

rem = 0

while number != 0:
    rem = rem * 10
    rem = rem + number % 10
    number = number // 10

print(f'reversed number is {rem}')
