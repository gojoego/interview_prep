class Queue:
    pass

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self, nodes):
        self.root = self.createBinaryTree(nodes)

    def createBinaryTree(self, nodes):
        if len(nodes) == 0:
            return None

        # Create the root node of the binary tree
        root = TreeNode(nodes[0].data)

        # Create a queue and add the root node to it
        queue = Queue()
        queue.put(root)

        # Start iterating over the list of nodes starting from the second node
        i = 1
        while i < len(nodes):
            # Get the next node from the queue
            curr = queue.get()

            # If the node is not None, create a new TreeNode object for its left child,
            # set it as the left child of the current node, and add it to the queue
            if nodes[i] is not None:
                curr.left = TreeNode(nodes[i].data)
                queue.put(curr.left)

            i += 1

            # If there are more nodes in the list and the next node is not None,
            # create a new TreeNode object for its right child, set it as the right child
            # of the current node, and add it to the queue
            if i < len(nodes) and nodes[i] is not None:
                curr.right = TreeNode(nodes[i].data)
                queue.put(curr.right)

            i += 1

        # Return the root of the binary tree
        return root

def solve_n_queens(n):
    results = [] # declare results array that will store all possible solutions for n queens 
    solution = [-1] * n # keeps track of current solution 
    place_queen(n, solution, 0, results) 
    
    # since no other queen can be in row that already has a queen, search for safe position for next queen in next row 
    # iterate over rows to find safe placement for queens
    # store column number where queen placed in list 
    # if safe position not found, backtrack to previous valid placement 
    # search for another solution 
    # if complete solution found, add to results array and backtrack to find other valid solutions in same way 
    return len(results)

def place_queen(n, solution, row, results): # start by placing queen in first column of first row of chess board 
    if row == n:
        results.append(solution[:])
        return 
    
    for i in range(0, n):
        valid = is_valid_move(row, i, solution)
        if valid:
            solution[row] = i
            place_queen(n, solution, row + 1, results)
            
# checks whether desired move can place queen at safe position
# move is valid if queen not vulnerable to attack from other queens on board
def is_valid_move(proposed_row, proposed_column, solution):
    for i in range(0, proposed_row):
        old_row = i
        old_column = solution[i]
        diagonal_offset = proposed_row - old_row
        if (old_column == proposed_column or 
            old_column == proposed_column - diagonal_offset or 
            old_column == proposed_column + diagonal_offset):
            return False
    return True

def solve_n_queens_stack(n):
    results = []
    solution = [-1] * n 
    queen_stack = []
    
    row = 0
    column = 0

    while row < n:
        while column < n:
            if is_valid_move(row, column, solution):
                queen_stack.append(column)
                solution[row] = column
                row = row + 1
                column = 0
                break
            column = column + 1
        if column == n:
            if queen_stack:
                column = queen_stack[-1] + 1
                queen_stack.pop()
                row = row - 1 
            else:
                break
        if row == n:
            results.append(solution[:])
            row = row - 1
            column = queen_stack[-1] + 1
            queen_stack.pop()
    return len(results)

  
def word_search(grid, word):
    n = len(grid) # numbers of rows in grid 
    m = len(grid[0]) # number of columns in grid 
    
    for row in range(n): # start traversing grid from first cell
        for column in range(m):
            # call DFS to find next character of search word in 4 possible directions for each grid cell 
            if depth_first_search(row, column, word, 0, grid):
                return True # word found
    return False # word not found 

def depth_first_search(row, column, word, index, grid):
    if len(word) == index: # if word has been found, base case
        return True
    
    # checking boundaries and character match 
    if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]) or \
        grid[row][column] != word[index]:
        return False
    
    # temporarily mark current cell as visited 
    temp = grid[row][column]
    grid[row][column] = '*'
    
    # if valid char found, call DFS function again for this cell 
    # explore 4 possible directions (right, down, left, up)
    for row_offset, column_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if depth_first_search(row + row_offset, column + column_offset, word, index + 1, grid):
            return True
    
    # continue searching through cell until either search word is found or all cells in grid visited 
    grid[row][column] = temp # restore original character in cell (backtracking)
    return False

def rob(root):
    return max(heist(root)) # returns max value from pair [include_root, exclude_root]

def heist(root):
    # if tree empty, return 0
    if root == None:
        return [0, 0]
    # recursively calculate max amount of money that can be robbed from left and right subtrees of root node 
    left_subtree = heist(root.left) # max amount from left 
    right_subtree = heist(root.right) # max amount from right 
    
    # recursively compute max amount of money that can be robbed with parent node included and excluded both 
    include_root = root.data + left_subtree[1] + right_subtree[1] # max if parent node included
    exclude_root = max(left_subtree) + max(right_subtree) # max if parent node excluded
    
    # return max from both amounts computed 
    return [include_root, exclude_root]

def restore_ip_addresses(s):
    # empty lists for storing valid IP addresses and each segment of IP 
    result = []
    segments = []
    
    backtrack(s, -1, 3, segments, result)
    # initially place all 3 dots each after 1 digit 
    # recursively add next digit from last segment to its previous segment 
    # if number in any segment exceeds 255, move digit to second segment 
    # make condition that checks whether each segment lies within 0 to 255 range
    # once all dots placed and each segment valid, return IP address 
    return result

def backtrack(string, previous_dot, dots, segments, result):
    # previous_dot - position of previously placed dot 
    # dots - number of dots in place

    size = len(string)
    
    # current dot can be placed in range from previous dot +1 to +4 
    # dot cannot be placed after last character in string 
    for current_dot in range(previous_dot + 1, min(size - 1, previous_dot + 4)):
        segment = string[previous_dot + 1: current_dot + 1]
        if valid(segment): # if segment acceptable 
            segments.append(segment) # add it to segments list 
            if dots - 1 == 0: # if all 3 dots placed, add solution to result 
                update_segment(string, current_dot, segments, result) 
            else: # continue to place dots 
                backtrack(string, current_dot, dots - 1, segments, result)
            segments.pop() # remove last placed dot 

def valid(segment):
    segment_length = len(segment) # store length of each segment 
    if segment_length > 3: # each segment length should be less than 3 
        return False

    # check if current segment valid for either one condition:
    # 1. check if current segment is less than or equal to 255
    # 2. check if length of segment is 1 - first character of segment can b 0 only if segment length == 1 
    return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

def update_segment(string, current_dot, segments, result):
    segment = string[current_dot + 1 : len(string)]
    if valid(segment):
        segments.append(segment)
        result.append('.'.join(segments))
        segments.pop() # remove top segment 

def flood_fill(grid, sr, sc, target):
    # for given source coordinates, check whether adjacent cells have same value as cell
    # if source cell already has same value as target, return original grid 
    # no need to iterate through whole grid in this case
    if grid[sr][sc] == target:
        return grid 
    else:
        # store original value of starting cell in in old target variable 
        old_target = grid[sr][sc] # will help in matching values of neighboring cells 
        grid[sr][sc] = target # replace value of starting cell with specified target 
        # call dfs function on starting cell to replace values of all connected cells 
        dfs(grid, sr, sc, old_target, target)
    # if any matching coordinate found, update value of that cell with given target 
    
    # value and proceed to next cell 
    # check adjacent coordinates 1 by 1, if they have same value as starting cell, keep
    # updating them by replacing cell's value with target value 
    # return updated grid after replacing values of cells that match source cell's value 
    return grid

def dfs(grid, row, column, old_target, new_target):
    # defining list of lists that reps 4 adjacent cells to start 
    # [0,1] move right, [1,0] move down, [-1,0] move up, [0,-1] move left 
    adjacent_cells = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    
    grid_length = len(grid) # length of grid
    total_cells = len(grid[0]) # length of each row (number of cells)
    
    # for each cell in list of adjacent cells
    for cell_value in adjacent_cells:
        i = row + cell_value[0]
        j = column + cell_value[1]
        
        # if adjacent cell within bounds of grid and has same value as start
        if i < grid_length and i >= 0 and j < total_cells and j >= 0 and grid[i][j] == old_target:
            grid[i][j] = new_target # replace value of adjacent cell with specified target
            dfs(grid, i, j, old_target, new_target) # recursively call dfs() on adjacent cell and repeat process  

def minimum_moves(grid):
    # store coordinates of cells with 0
    # store coordinates and number of extra stones in cells with 1+ stones 
    zeros = []
    extras = []
    min_moves = float('inf')
    
    # calculate total number of stones 
    total_stones = sum(sum(row) for row in grid)
    if total_stones != 9: # return -1 if total stones not exactly 9 
        return -1 
    
    def solve(i, count): # fxn to solve problem using backtracking 
        if i >= len(zeros):
            nonlocal min_moves
            min_moves = min(min_moves, count)
            return
        for k in range(len(extras)):
            if extras[k][2] != 0:
                extras[k][2] -= 1
                solve(i + 1, abs(extras[k][0] - zeros[i][0]) + abs(extras[k][1] - zeros[i][1]) + count)
                extras[k][2] += 1
    
    for x in range(3): # populate zeros and extras arrays 
        for y in range(3):
            if grid[x][y] == 0:
                zeros.append([x,y])
            elif grid[x][y] > 1:
                extras.append([x, y, grid[x][y] - 1])
    
    if len(zeros) == 0:
        return 0
    
    solve(0, 0)
    return min_moves

    

    # recursively fill empty cells with excess stones 
    # calculate min moves required for each possible redistribution 
    # after exploring particular redistribution path, backtrack to 
    # previous state and explore other possible paths 
    # after exploring all possible paths, return min number of moves 

DIGITS = ['1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    
def solve_sudoku(board):
    solve(board)
    return board

def solve(board):
    # start iterating board from top left cell until reaching first free cell 
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for num in DIGITS:
                    # place numbers between 1 to 9 in current cell 
                    # if number isn't already present in current row, column, and 3x3 sub-box 
                    if is_valid(board, i, j, num):
                        board[i][j] = num # write down that number that is now present in current row, column, and box 
                        # backtrack if solution not yet present and remove last number from cell 
                        if solve(board): # if we reach last cell, solved! 
                            return True
                        board[i][j] = '.' # else move on to next cell 
                return False
    return True
    
def is_valid(board, row, column, number):
    for i in range(9): # checking if number already in current row
        if board[row][i] == number:
            return False
        
    for i in range(9): # check if number already in current column 
        if board[i][column] == number:
            return False
    
    # find start indices of 3x3 sub-box
    start_row, start_column = 3 * (row // 3), 3 * (column // 3)
    # check if number in current 3x3 sub-box 
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_column + j] == number:
                return False
    return True
    
def matchstick_to_square(matchsticks):
    # if number of matchsticks less than 4 or sum not multiple of 4
    if len(matchsticks) < 4: # impossible to form square, return false 
        return False
    
    total_length = sum(matchsticks) # calculate total length of all matchsticks 
    
    if total_length % 4 != 0: # if total length is not divisible by 4
        return False # square cannot be formed, return False
    
    # sort matchsticks in descending order and set length of one side of square
    # to 1/4th of sum of all values in matchsticks 
    matchsticks.sort(reverse=True)
    side_length = total_length // 4
    
    # if any single matchstick longer than side of square, return False 
    if matchsticks[0] > side_length:
        return False
    
    # create list to track length of 4 sides, initialize to [0,0,0,0]
    sides = [0,0,0,0]
    
    # start backtracking process from first matchstick 
    return backtrack(matchsticks, sides, 0, side_length)

# defining backtracking function
def backtrack(matchsticks, sides, index, side_length):

    # base case: if all matchsticks used
    if index == len(matchsticks): # check if all 4 sides equal length, return true/false 
        return sides[0] == sides[1] == sides[2] == sides[3] == side_length
    
    # use validate function to check if placing current matchstick valid 
    return validate(matchsticks, sides, index, side_length)

def validate(matchsticks, sides, index, side_length):
    # iterate through list of 4 sides 
    for i in range(4):
        # if sum of matchsticks[index] + current side length is less than or equal to target side length
        if sides[i] + matchsticks[index] <= side_length:
            sides[i] += matchsticks[index] # update current side by adding matchsticks[index]
            # recursively call backtracking function with next index
            if backtrack(matchsticks, sides, index + 1, side_length):
                return True 
            # undo previous addition to side length by subtracting matchsticks[index] 
            # and move on checking if current matchstick
            sides[i] -= matchsticks[index] 
            
    # return false if no combo of matchsticks results in valid square after trying all possible combos 
    return False