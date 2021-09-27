# check for equivalence relation

R = [[1, 1, 0],
     [1, 1, 1],
     [0, 1, 1]]

matrix = [ [ 1, 0, 0, 1, ...], [0, 1, ...], ...]
assert all(len(row)==len(matrix) for row in matrix) # check whether both dimensions are the same
if all(matrix[i][i] == 1 for i in range(len(matrix))):
    print("Relation is reflexive")
else:
    print("Relation is not reflexive")


def reflexiveTest(R):


    count = 0
    for i in range(3):
        if R[i][i] == 1:
            count = count + 1
    return count

def symmetricTest(R):
    for k in range(len(R)):
        for l in range(len(R)):
            print("Test")


x = reflexiveTest(R)

if x == 0:
    print("Irreflexive")
elif x in range(len(R)):
    print("Not reflexive")
elif x == len(R):
    print("Reflexive")










# if count == len(R):
#     print("Reflexive")
# else:
#     print("Not reflexive")


