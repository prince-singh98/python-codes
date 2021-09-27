num = 7
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for trial in range(3):
    ans = int(input("enter a num : "))
    if ans in list:
        if trial == 0 or trial == 1:
            if ans == num:
                print("success")
                break
            else:
                print("try again")

        elif trial == 2:
            if ans == num:
                print("success")
                break
            else:
                print("You lost the game! ")

    else:
        print("Please select any one from 0 to 9")
        break



