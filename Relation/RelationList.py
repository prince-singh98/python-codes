A = {"A", "B", "C"}


def is_symmetric(relation):
    for a, b in relation:
        if (a,b) in relation and (b,a) in relation and a != b:
            return "Symmetric"
    return "Asymmetric"

print(is_symmetric([("A","A"), ("A","C"), ("C","A"), ("C","C")])) # True
print(is_symmetric([("A","A"), ("A","C"), ("A","B"), ("C","C")])) # False



def is_reflexive(relation):
    if all((a,a) in relation for a in A):
        return "reflexive"
    return "not reflexive"


print(is_reflexive([("A","A"), ("A","C"), ("B","B"), ("A","B"), ("C","C")])) # True
print(is_reflexive([("A","A"), ("A","C"), ("C","A"), ("C","C")])) # False
print(is_reflexive([("A","C"), ("A","B")])) # False


def is_transitive(relation):
    for (a, b) in relation:
        for (c, d) in relation:
            if b == c and (a, d) in relation:
                return "transitive"
        return "not transitive"

print(is_transitive([("A","B"), ("A","C"), ("B","C"), ("A","B"), ("C","C")])) # True
print(is_transitive([("A","B"), ("B","C"), ("A","B"), ("C","C")])) # False


