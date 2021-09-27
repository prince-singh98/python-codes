
# fibonacci series wrt term

term = int(input("enter up to which term you want: "))
t1 = 0
t2 = 1
print(t1)
print(t2)

for x in range(2,term,1):
    nextTerm = t1 + t2
    print(nextTerm)
    t1 = t2
    t2 = nextTerm
