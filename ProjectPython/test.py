mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(len(mat)):  # n
    for j in range(len(mat[i])): # n
        print(mat[i][j], end=",") # n * n => n2
    print()

for i in range(len(mat[0])):
    print(mat[1][i])