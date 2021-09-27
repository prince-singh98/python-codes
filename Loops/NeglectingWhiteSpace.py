str = "i am a developer"
print(len(str))

for x in range(len(str)):
    if str[x] == " ":
        continue
    else:
        print(str[x])
