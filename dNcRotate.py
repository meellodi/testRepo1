from math import floor


def dNcRotate(matrix):
    l = len(matrix)
    for j in range(0, floor(l/2)):
        for i in range(j, l-1-j):
            x = j
            y = i
            prev = matrix[x][y]
            for k in range(4):
                # print(x, y)
                # print(x, y, matrix[x][y])
                z = x
                x = y
                y = l-1-z
                temp = matrix[x][y]
                matrix[x][y] = prev
                prev = temp
            # print(x, y)
    print(matrix)


matrix = [[0, 1], [2, 3]]
matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
dNcRotate(matrix)
