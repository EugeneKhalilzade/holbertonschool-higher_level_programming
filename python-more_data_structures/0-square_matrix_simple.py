#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newtrix = []
    for rows in matrix:
        newrows = []
        for i in rows:
            newrows.append(i*i)
        newtrix.append(newrows)
    return newtrix
