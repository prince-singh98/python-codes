
def myFunction():
    print("my fuction")

myFunction()


def moveForward(instruct):
    if instruct == "Key1":
     print("success")
     return 1
    return -1


press="Ke1"
press1="Key2"
status=moveForward(press)
print("status",status)