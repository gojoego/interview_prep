'''

matrix transformations: operations performed on matrices that result in new matrix 
    -addition and subtraction 
    -multiplication
    -inverse
    -transpose
    -scalar multiplication
    -rotation 
    -reflection 

matrix traversal: process of systematically visiting each element in matrix exactly once
    -common in searching, sorting, pathfinding and data manipulation
    -row-major traversal: row by row horizontally then vertically
    -column-major traversal: column by column vertically then horizontally
    -diagonal traversal: along diagonal elements, main or secondary 
    -spiral traversal: spiral pattern, outmost to innermost to center 

common matrix problems 
    -rotate and invert image 
    -Toeplitz matrix: every descending diagonal from left to right has same elements 

criteria for matrix pattern problems: 2D array input 

real-world problems
    -image processing 
    -computer graphics and gaming
    -data analysis and statistics 
    -machine learning     

'''

def print_matrix(matrix):
    for row in matrix:
        print(row)
 
def naive_set_matrix_zeros(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    
    # create copy of original matrix 
    copy = [[matrix[i][j] for j in range(columns)] for i in range(rows)]
    
    # traverse matrix and set rows and columns in copy to 0 if 0 found in matrix 
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 0:
                # set entire row in copy to 0
                for k in range(columns):
                    copy[i][k] = 0
                # set entire column in matrix to 0
                for k in range(rows):
                    matrix[k][j] = 0

    # copy all elements of copy back to matrix 
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = copy[i][j]
    
    return matrix

def set_matrix_zeros(mat):
    rows = len(mat)
    columns = len(mat[0])
    fcol = False
    frow = False
    
    # if any element in first row and/or first column 0, set frow and fcol to True
    for i in range(rows):
        if mat[i][0] == 0:
            fcol = True
    
    # check if 0 in first row, set frow to True
    for i in range(columns):
        if mat[0][i] == 0:
            frow = True 
            
    # scan complete matrix row-wise by ignoring first row and column 
    # set 0 in first element of particular row and column where 0 is found
    for i in range(1, rows):
        for j in range(1, columns):
            if mat[i][j] == 0:
                mat[0][j] = mat[i][0] = 0
                
    # check every row's first element, starting from second row
    # if 0, set all values in that row to 0
    for i in range(1, rows):
        if mat[i][0] == 0:
            for j in range(1, columns):
                mat[i][j] = 0
                
    # check every column's first element starting from second column
    # if 0, set all values in column to 0
    for j in range(1, columns):
        if mat[0][j] == 0:
            for i in range(1, rows):
                mat[i][j] = 0
    
    # if frow and/or fcol True, set first row or column to 0
    if fcol:
        for i in range(rows):
            mat[i][0] = 0
    
    if frow:
        for j in range(columns):
            mat[0][j] = 0        
    
    return mat

# given n x n matrix, rotate 90 degrees clockwise in place 
def rotate_image(matrix):
    
    n = len(matrix)
    
    # traverse groups of 4 cells in matrix, starting from four corners 
    for row in range(n // 2): 
        for col in range(row, n - row - 1):
            # swap top-left cell with top-right cell in current group 
            matrix[row][col], matrix[col][n - 1 - row] = matrix[col][n - 1 - row], matrix[row][col]
            # swap top-left cell with bottom-right cell in current group 
            matrix[row][col], matrix[n - 1 - row][n - 1 - col] = matrix[n - 1 - row][n - 1 - col], matrix[row][col]
            # swap top-left cell with bottom-left cell in current group 
            matrix[row][col], matrix[n - 1 - col][row] = matrix[n - 1 - col][row], matrix[row][col]
            # move to next group of four cells and repeat steps 
            
    return matrix

def spiral_order(matrix):
    # calculate total number of rows and columns 
    rows = len(matrix)
    cols = len(matrix[0])
    
    # declare variable, direction, which stores either 1 (for going left to right and top to bottom)
    # or -1 (for going right to left and bottom to top)
    direction = 1
    
    # declare 2 variables, row and col (both initialized to 0) to track current indices of matrix 
    row = 0
    col = -1
    
    # create array to store elements in spiral order 
    result = []
    
    # start traversing matrix from top-left
    while rows > 0 and cols > 0:
        # move horizontally across row by adding direction to col variable while keeping row unchanged
        # 1. left to right (if direction == 1)
        # 2. right to left (if direction == -1)
        for _ in range(cols):
            # increment col pointer to move horizontally
            col += direction
            # add matrix[row][col] to result array 
            result.append(matrix[row][col])
        rows -= 1 
        
        # move vertically across column by adding direction to row variable while keeping col unchanged 
        # 1. top to bottom (if direction == 1)
        # 2. bottom to top (if direction == -1)
        for _ in range(rows):
            # increment row pointer to move vertically
            row += direction  
            # add matrix[row][col] to result array
            result.append(matrix[row][col]) 
        cols -= 1
              
        # flip direction by multiplying direction variable by -1 
        direction *= -1
        # repeat process until all cells traversed 
        
    return result

def main():
    inputs = [[[1]], [[6], [2]], [[2, 14, 8], [12, 7, 14]],
              [[3, 1, 1], [15, 12, 13], [4, 14, 12], [10, 5, 11]],
              [[10, 1, 14, 11, 14], [13, 4, 8, 2, 13], [10, 19, 1, 6, 8], [20, 10, 8, 2, 12], [15, 6, 8, 8, 18]]]

    for i in range(len(inputs)):
        print(i + 1, ".\tMatrix:", sep="")
        print_matrix(inputs[i])

        print("\n\tSpiral order:", spiral_order(inputs[i]))
        print("-" * 100)
          
if __name__ == "__main__":
    main()