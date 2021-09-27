# number = int(input("enter a number: "))
# if(number == 0):
#     print(f'{number} is neither even nor odd')
# elif(number%2 == 0):
#     print(f'{number} is even')# formated string
# else:
#     print(f'{number} is odd')

num = int(input("enter a number: "))

if num == 0:
    print(f'{num} is neither odd nor even')
else:
    if num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

