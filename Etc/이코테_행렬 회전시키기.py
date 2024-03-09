data = [[1,2],[3,4]]
def rotate_90_degree(data):
    col = len(data)
    row = len(data[0])
    new_matrix = [[0]*col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            new_matrix[i][col - j -1] = data[j][i]
    print(new_matrix)


rotate_90_degree(data)