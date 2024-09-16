'''

stack
-linear data structure that organizes and manages data LIFO like a stack of plates
-2 fundamental operations
    push: element placed on top of stack 
    pop: removing top element 
-capacity
    stack overflow: trying to push element onto full stack 
    stack underflow: trying to pop element from empty stack 
-capacity issues can result in memory-related issues (crash or error)
-all stack operations are O(1) time 
-other stack operations
    peek: returns top element without removal 
    isEmpty: boolean that checks for empty stack 
    size: returns number of elements in stack 
-array implementation
    -fixed-size array where elements added/removed from one end 
    -pointer or index variable used to keep track of top of element stack
    -push increments pointer, pop decrements 
-linked list based implementation 
    -elements of stack rep by node in list 
    -each node contains data and reference to next node 
    -top of stack is head or first node in list 
    -push adds elements to beginning of list, pop removes head node 
-used for...
    -storing elements with sequential dependencies in expressions or algorithms 
    -ensure safe storage without arbitrary modification from middle positions 
    -repeatedly modifying stream of elements based on specific conditions 
-examples:
    -reverse string using stack
    -evaluate postfix expression 
-does your problem match stack pattern? 
    yes, if...
    -reverse order processing
    -nested structures handling
    -state tracking 
    -expression evaluation 
    no, if...
    -order dependence
    -random access 
    -need for searching 
-real world examples:
    -function call stack 
    -text editor undo/redo feature 
    -browser back and forward buttons 
    -call history in smartphones 

'''
# create function that calculates string containing arithmetic expression 
def calculator(expression):
    # initialize stack to manage nested expressions 
    # and 3 variables for current number, sign value, result
    operations = []
    number = 0
    sign_value = 1
    result = 0
    
    # iterate through input string to process equation
    for c in expression:
        # determine if character is a digit, parenthesis or operator 
        
        # when encountering digit, update number variable by appending digit to it
        if c.isdigit():
            number = number * 10 + int(c)
        
        # for operators (+ and -), compute left expression using current sign and update result
        if c in "+-":
            result += number * sign_value
            sign_value = -1 if c == '-' else 1
            number = 0
        
        # if opening parenthesis found, push current result and sign onto stack for nested expressions
        elif c == '(':
            operations.append(result)
            operations.append(sign_value)
            result = 0
            sign_value = 1
        
        # closing parenthesis, compute expression within it and update result 
        elif c == ')':
            result += sign_value * number
            pop_sign_value = operations.pop()
            result *= pop_sign_value
            
            second_value = operations.pop()
            result += second_value
            number = 0

    # once whole expression traversed, return final result, which represents
    # evaluated arithmetic expression 
    
    return result + number * sign_value

# create function that removes duplicates in a given string 
# time O(n^2), space O(n)
def naive_remove_duplicates(s):
    found_duplicates = True
    
    while found_duplicates:
        found_duplicates = False
        result = []
        
        # traverse string, comparing adjacent characters 
        i = 0
        while i < len(s):
            # if current character same as next one, skip both 
            if i < len(s) - 1 and s[i] == s[i + 1]:
                found_duplicates = True # found pair to remove 
                i += 2
            else:
                # if no duplicate, add character to result
                result.append(s[i])
                i += 1
        # update string with modified result
        s = ''.join(result)
        
    return s

# time O(n), space O(n)
def remove_duplicates(s):
    # initialize stack to store characters 
    characters = []
    
    # traverse every character in string 
    for char in s:
        # in each iteration, if string char same as char at top of stack, pop 
        if characters and characters[-1] == char:
            characters.pop()
        # if string char different from char at top of top, push char onto stack
        else:
            characters.append(char)
    # after all iterations, form string from characters in stack and return 
    return ''.join(characters)