number = int(input("enter a number: "))

m = number//2

if number > 1:
    for x in range(2, m):
        if (number % x) == 0:

            print(f'{number} is not prime number')
            break
    else:
        print(f'{number} is a prime number')

else:
    print(f'{number} is not a prime number')
