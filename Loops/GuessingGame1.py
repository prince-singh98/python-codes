# guessing limit is 0-10

markedValue = 6
print("<-Guessing Game->")
print("Note:The guessing range betwn 0-10")

for chance in range(3):
    guessNo = int(input("Enter your Guess :"))
    if guessNo <= 10:
        if guessNo == markedValue:
            print("Won!! ")
            break;
        else:
            print("try some more chances")
    else:
        print("Try your options betwn 0-10 ")

if (chance >= 2):
    print("U exausted ur chance")