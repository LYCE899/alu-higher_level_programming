#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
matrix=[[1,2,3],[4,5,6],[7,8,9]]
    for row in matrix:
        for i in row:
            if i != row[len(row) - 1]:
                print("{:d}".format(i), end=" ")
            else:
                print("{:d}".format(i), end=" ") 
        print()
