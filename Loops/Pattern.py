# to draw pattern given below
# *
# **
# ***
# ****
# *****

# first solution
for x in range(6):
    for y in range(x):
        print("*", end='')
    print("")

# second solution
for x in range(5):
    print((x+1)*'#')

# to draw pattern given below

# *****
# **
# *****
# **
# **

for x in range(5,0,-1):
    if x == 5 or x == 3:
        print(5*'*')
    else:
        print(2*'*')

for x in range(5, 0, -1):
    print(x * '#')

# 1
# 12
# 123
# 1234
# 12345

for x in range(2,7,1):
    for y in range(1,x,1):
        print(y, end='')
    print("")


# A
# AB
# ABC
# ABCD
# ABCDE

str="A"
for x in range(5):
    for y in range(x):
        print((chr(ord(str)+y)),end="")
    print("")