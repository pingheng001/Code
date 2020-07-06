# -*- coding:utf-8 -*-

def parse_position(x):
    result = x % 10
    while x / 10 > 0:
        x = x / 10
        result += x % 10
    return result

def get_x_y_sum(i, j):
    return parse_position(i) + parse_position(j)

def move(networks, row, col, threshold):
    network_rows = len(networks)
    network_cols = len(networks[0])
    if row < 0 or row >= network_rows or col < 0 or col >= network_cols:
        return
    if networks[row][col] == 1:
        return
    if networks[row][col] == 0 and get_x_y_sum(row, col) <= threshold:
        networks[row][col] = 1
    else:
        return
    move(networks, row - 1, col, threshold)
    move(networks, row + 1, col, threshold)
    move(networks, row, col - 1, threshold)
    move(networks, row, col + 1, threshold)

def movingCount(threshold, rows, cols):
    networks = []
    for i in range(rows):
        networks.append([])
        for j in range(cols):
            networks[i].append(0)
    move(networks, 0, 0, threshold)
    sum = 0
    for i in range(rows):
        for j in range(cols):
            if networks[i][j] == 1:
                sum += 1
    return sum

print movingCount(5,10,10)