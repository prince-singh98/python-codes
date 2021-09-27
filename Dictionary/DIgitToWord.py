dictionary = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

number = int(input("Enter a number : "))
if number in dictionary.keys():

    print("yes")
    print(dictionary.get(number))
else:
    print("Sorry! Out of range")

# second solution

# inp=int(input("Enter your no :"))
# if dict.get(inp):
#     print(dict.get(inp))
# else:
#     print("sorry try from above")




#
# if number>"0" and number<"10":
#
#     if number in dictionary.keys():
#         print(dictionary.get(number))
#
# else:
#     print("sorry")

