# global scope
Scope = 21


def scopeCheck():
    # accessing global scope variable
    print(Scope)
    scope = 25
    # printing local scope variable
    print(scope)


scopeCheck()
