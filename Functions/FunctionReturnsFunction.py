
# def f1():
#     print("fun1")
#
#
# def f2():
#     return f1()
#
#
# f2()

# def f1():
#
#     def f2():
#         print("hello!")
#     return f2()
#
# f1()

def f1():
    print("f1 function")
    def f2():
        print("f2 function")
    return f2

f2=f1()

f2()