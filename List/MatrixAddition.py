matrix1 = [[1,2,3], [4,5,6], [7,8,9]]
matrix2 = [[10,11,12], [13,14,15], [16,17,18]]
result = [[0,0,0], [0,0,0], [0,0,0]]

for row in range(len(matrix1)):
    for col in range(len(matrix2)):
        result[row][col] = matrix1[row][col] + matrix2[row][col]

print(matrix1)
print(matrix2)

for r in result:
    print(r)
