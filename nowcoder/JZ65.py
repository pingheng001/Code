# -*- coding:utf-8 -*-


def path_match(matrix, networks, row, col, path, current_path):
    matrix_rows = len(matrix)
    matrix_cols = len(matrix[0])
    if row < 0 or row >= matrix_rows or col < 0 or col >= matrix_cols:
        return False
    if networks[row][col] == 1:
        return False
    current_path += matrix[row][col]
    if current_path == path:
        return True

    has_path = False
    if current_path == path[:len(current_path)]:
        networks[row][col] = 1
        left = path_match(matrix, networks, row, col-1, path, current_path)
        right = path_match(matrix, networks, row, col+1, path, current_path)
        up = path_match(matrix, networks, row+1, col, path, current_path)
        low = path_match(matrix, networks, row-1, col, path, current_path)
        has_path = left or right or up or low
        if not has_path:
            networks[row][col] = 0

    return has_path

def hasPath(matrix_str, rows, cols, path):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(matrix_str[i*cols+j])


    networks = []
    for i in range(rows):
        networks.append([])
        for j in range(cols):
            networks[i].append(0)
    has_path = False
    for i in range(rows):
        for j in range(cols):
            result = path_match(matrix, networks, i, j, path, '')
            if result:
                has_path = True
                break
        if has_path:
            break
    return has_path



# matrix = [['a', 'b', 'c', 'e'], ['s', 'f', 'c', 's'], ['a', 'd', 'e', 'e']]

# matrix_rows = len(matrix)
# matrix_cols = len(matrix[0])
# print matrix
print hasPath('AAAAAAAAAAAA', 3, 4, 'AAAAAAAAAAAA')