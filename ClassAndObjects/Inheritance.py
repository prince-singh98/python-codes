class Bird:#parent
    def WhoIsThis(self):
        print("penguin")

class Penguin(Bird):
    def WhoIsThis(self):
        print("peg")
    print("xyz")

peg=Penguin()
print(peg.WhoIsThis())
