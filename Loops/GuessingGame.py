
num = 7

for trial in range(3):
    ans = int(input("enter a num : "))

    if trial in range(2):
        if ans == num:
            print("success")
            break
        else:
            print("try again")

    else:
        if ans == num:
            print("success")
            break
        else:
            print("You lost the game! ")
