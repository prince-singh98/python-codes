A = {1, 2, 3}


R = {(1, 1), (1, 2), (1, 3), (2, 1), (2, 2), (2, 3), (3, 1), (3, 2), (3, 3)}


def is_reflex_notReflex_Irreflex(R):

    count = 0
    for a, b in R:
        if (a, b) and a == b:
            count += 1
    if count == 0:
        # Ir-reflexive relation
        return count
    if count == len(A):
        # Reflexive relation
        return count
    # Not reflexive relation
    return count


def is_symmetric(R):

    for a, b in R:
        if (b, a) not in R:
            return False
    return True


def is_not_symmetric(R):

    for a, b in R:
        if (a, b) in R and (b, a) not in R:
            return True
    return False


def is_anti_symmetric(R):
    # checks Anti-Symmetric
    status = False
    for a, b in R:
        if (a, b) in R and (b, a) in R:
            if a == b:
                status = True
    return status


def is_transitive(R):
    for a, b in R:
        for c, d in R:
            if b == c and (a, d) not in R:
                return False
    return True


def check_equivalence(R):
    return is_symmetric(R) and is_transitive(R) and is_reflex_notReflex_Irreflex(R) == len(A)


def partial_order(R):
    return is_anti_symmetric(R) and is_transitive(R) and is_reflex_notReflex_Irreflex(R) == len(A)


result = is_reflex_notReflex_Irreflex(R)
if result == len(A):
    print("R is reflexive")
elif result == 0:
    print("R is not Ir reflexive")
else:
    print("R is not reflexive")

result = is_symmetric(R)
if result is True:
    print("R is symmetric")

result = is_not_symmetric(R)
if result is True:
    print("R is not symmetric")

result = is_anti_symmetric(R)
if result is True:
    print("R is anti symmetric")


result = is_transitive(R)
if result is True:
    print("R is transitive")
else:
    print("R is not transitive")

result = check_equivalence(R)
if result is True:
    print("R is a Equivalence Relation")
else:
    print("R is not a Equivalence Relation")

result = partial_order(R)
if result is True:
    print("R is partial order")
else:
    print("R is not partial order")
