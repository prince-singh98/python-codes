def make_preety(func):
    def inner():
        print("I got decoratred")
        func()
    return inner


def ordinary():
    print("I am ordinary")


preety = make_preety(ordinary)

preety()
