def read_matrix(rows, cols):
    print(f"Enter the elements for a {rows}x{cols} matrix row-wise:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print(f"Error: Please enter exactly {cols} values per row.")
            return read_matrix(rows, cols)  # Ask for input again if incorrect
        matrix.append(row)
    return matrix


def matrix_multiplication(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):  # or rows_B (since cols_A == rows_B)
                result[i][j] += A[i][k] * B[k][j]

    return result


# Read matrix dimensions from user
rows_A = int(input("Enter number of rows for Matrix A: "))
cols_A = int(input("Enter number of columns for Matrix A: "))

rows_B = int(input("Enter number of rows for Matrix B: "))
cols_B = int(input("Enter number of columns for Matrix B: "))

# Ensure matrices can be multiplied
if cols_A != rows_B:
    print("Error: Number of columns in Matrix A must be equal to number of rows in Matrix B.")
else:
    # Read matrices from user
    A = read_matrix(rows_A, cols_A)
    B = read_matrix(rows_B, cols_B)

    # Perform matrix multiplication
    result = matrix_multiplication(A, B)

    # Print result
    print("Resultant Matrix:")
    for row in result:
        print(" ".join(map(str, row)))
