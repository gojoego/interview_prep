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