import sys

def matrix_multiplication(matrix1, row1, matrix2, col2, col1):
    result_matrix = []

    for row in range(row1):
        result_row = []
        for col in range(col2):
            product = 0
            for i in range(col1):
                product += matrix1[row][i] * matrix2[i][col]   # see the definition of matrix multiplication
            result_row.append(product)
        result_matrix.append(result_row)

    return result_matrix


while True:
    row1 = int(input("enter row of first matrix: "))
    col1 = int(input("enter column of first matrix: "))
    row2 = int(input("enter row of second matrix: "))
    if row2 != col1:
        print("col1 and row2 does not match, enter again or terminate: ")
        col1 = int(input("enter column of first matrix: "))
        row2 = int(input("enter row of second matrix: "))
    col2 = int(input("enter column of second matrix: "))

    matrix1 = []
    matrix2 = []

    print()
    print("enter the matrix 1 inputs: ")
    for i in range(row1):
        row = list(map(int, sys.stdin.readline().split()))
        if len(row) != col1:
            print("wrong number of columns, exit programme and re-enter")
        else:
            matrix1.append(row)

    print()
    print("enter the matrix 2 inputs: ")
    for i in range(row2):
        row = list(map(int, sys.stdin.readline().split()))
        if len(row) != col2:
            print("wrong number of columns, exit programme and re-enter")
        else:
            matrix2.append(row)
    

    print(matrix_multiplication(matrix1, row1, matrix2, col2, col1))
    print()
