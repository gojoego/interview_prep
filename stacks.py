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

def calculator(s):

    # Replace this placeholder return statement with your code
    return 0