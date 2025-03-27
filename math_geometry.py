'''
math and geometry pattern:
- mathematical concepts, geometric properties, and coordinate systems 
- analyzing numbers, points, lines, angles and shapes in 2D or 3D space 
- helps with tasks related to distances, areas, and coordinate-based computations
- emphasizes the importance of algorithmic efficiency
- brute force approach might require evaluating all combinations of numbers, points, 
    or shapes—potentially leading to high computational costs
- recognizing and applying optimal techniques, such as the two-pointer approach, 
    can significantly reduce runtime and make solutions far more effective

elementary number theory 
- focuses on integer properties and relationships
- greatest common divisor (GCD): to calculate the GCD of two numbers a and b, repeatedly apply 
    gcd(a, b) = gcd(b, a mod b) until b = 0; the final non-zero value of a is the greatest common 
    divisor; this method is known as Euclid's algorithm
- least common multiple (LCM): LCM of two numbers can be calculated as: lcm(a,b) = a * b / gcd(a,b)

advanced integer handling
- involves manipulating integers that may push the limits of standard integer data type, such as 
    adding or multiplying large numbers or reversing integers
- operations are often performed digit by digit to avoid overflow and ensure precision

distance between points
- calculating how far apart two points are on a 2D plane
- for two points, (x1, y1) and (x2, y2), distance calculated using: 
        Euclidean distance: math.sqrt(x2 - x1) ^ 2 + (y2 - y1) ^ 2)
        Manhattan distance: |x2 - x1| + |y2 - y1|

slope calculation: 
- measuring the steepness of a line between two points, paying attention to vertical lines
- for two points, (x1, y1) and (x2, y2), the slope is calculated as: m = (y2 - y1) / (x2 - x1)
- special care is needed when x2 = x1 (i.e., a vertical line)

angle measurement: 
- computing angles between lines or points, often using the inverse tangent function.
- using arctan: angle is calculated as θ = arctan((y2 - y1) / (x2 - x1)) 
- atan2: angle is computed as θ = atan2(y2 - y1, x2 - x1) -> preferred as it properly handles 
    all quadrants and avoids division by zero errors

polygon geometric attributes:
- focuses on calculating side lengths, angles (interior or exterior), area, and perimeter 
    for polygons

polygon spatial attributes
- involves verifying polygon properties such as convexity or orientation
- convexity check: use the sign of the cross product for every trio of consecutive vertices to 
    ensure all interior angles are less than 180°
- orientation: check the clockwise or counterclockwise order of vertices using the sign of 
    the cross product

validate polygons:
- focuses on determining if a set of points forms a valid polygon, such as a triangle or square
- for example, a square requires:
        - all four sides are equal
        - both diagonals are equal

examples
- check if it a straight line 
- valid square 
- given 2 rectangles, each defined by its bottom-left and top-right corners, find 
    total area covered by both rectangles 
- given array of points on 2D plane, return min time in seconds needed to visit all points 
    in specified order 

does your problem match this pattern? yes, if...
- elementary number theory
- advanced integer handling 
- point-based calculations 
- polygon attributes

real-world problems
- geospatial navigation (GPS and mapping)
- urban planning and property layout
- robotics and path panning 


'''

'''
Check If It Is a Straight Line

statement: you are given an array, coordinates, where each element in coordinates[i] = [x,y]
represents the coordinates of a point on a 2D plane; determine whether all the points in the 
array lie on a single straight line in the XY plane

algorithm: 
- slope: represents change in y-coordinates to relative to change in x-coordinates for any 2 
    points on line
    
    2 points (x1,y1) and (x2,y2), slope = y2 - y1 / x2 - x1 
    
- straight line slope must remain constant 
- fix first point as reference and compute slopes between reference point and all other 
    points instead of checking all possible pairs of points 
- to avoid division-related issues, use cross-multiplication approach to compare slopes -> 
    eliminates need for division -> deltas y1 * x2 = y2 * x1 (ensures numerical precision is 
    maintained and special cases handled seamlessly)  

    

time O(n) where n = array length, space O(1)
'''

def check_straight_line(coordinates):
        # calculate initial differences for first 2 points 
        deltaX1 = coordinates[1][0] - coordinates[0][0]
        deltaY1 = coordinates[1][1] - coordinates[0][1]
        
        # iterate through remaining points 
        for i in range(2, len(coordinates)):
                # calculate differences for current point relative to first point 
                deltaX2 = coordinates[i][0] - coordinates[0][0]
                deltaY2 = coordinates[i][1] - coordinates[0][1]
                
                # use cross-multiplication to check for collinearity 
                if (deltaY1 * deltaX2) != (deltaX1 * deltaY2):
                        return False
        
        # if all points collinear, return True 
        return True 

'''
Minimum Cuts to Divide a Circle

statement: given an integer n, determine the minimum number of cuts required to divide the 
circle into n equal slices; a valid cut in a circle is defined as one of the following:

    - a cut is represented by a straight line that passes through the circle's center and touches 
      two points on its edge
    - a cut is represented by a straight line touching one point on the circle's edge and center

algorithm: 
- if n = 1, no cuts return 0 
- if n > 1 and even, circle can be divided into n slices by making n / 2 cuts passing through center
- if n odd, make n cuts so that each cut forms 1 slice  

'''
def number_of_cuts(n):
    # if n = 1, return 0 since no cuts are required to divide circle into 1 slice 
    if n == 1:
        return 0 

    # next, if n greater than 1 / odd, return n since n cuts required to divide circle into n slices 
    if n % 2 == 1:
        return n 
    
    # if n even, number of cuts is half of n 
    return n/2 

'''
Rectangle Overlap

statement: an axis-aligned rectangle is represented by a list [x1,y1,x2,y2] where 
    - (x1,y1) denotes the coordinates of the bottom-left corner
    - (x2,y2) denotes the coordinates of the top-right corner

the rectangle's sides are aligned with the axes:
    - the top and bottom edges are parallel to the X-axis
    - the left and right edges are parallel to the Y-axis

note: two rectangles are considered to overlap if their intersection forms a region with a 
positive area; rectangles that touch only at the edges or corners are not considered to overlap

determine if the two axis-aligned rectangles, rec1 and rec2, overlap; return TRUE if they overlap; 
otherwise, return FALSE

algorithm: 
- determine interval overlaps for x and y axis projections 
- overlap corresponds to projection overlap to form region with positie width and height 
- intersection width (x-axis overlap) and height (y-axis overlap)
- the overlap along the x-axis is positive when:

  min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])

- rec1[0] and rec2[0] are the left boundaries, while rec1[2] and rec2[2]
  are the right boundaries of the rectangles
- ensures that the smaller of the two rectangles' right boundaries is greater than the 
  larger of their left boundaries
- overlap along the y-axis is positive when:
  
  min(rec1[3], rec2[3]) > max(rec1[1], rec2[1])

- rec1[1] and rec2[1] are the bottom boundaries, while rec1[3] and rec2[3] are the top 
  boundaries of the rectangles
- ensures that the smaller of the two rectangles' top boundaries is greater than the larger 
  of their bottom boundaries

- reduction to 1D interval overlap: the problem is reduced to determining whether two line
  segments overlap in 1D space; for an axis-aligned rectangle:
    
    - the width is the overlap of its x-axis projection
    - the height is the overlap of its y-axis projection

- the width and height overlaps must be positive for the rectangles to overlap
- if either overlap is zero or negative, the rectangles do not overlap

time and space O(1)
'''
def is_rectangle_overlap(rec1, rec2):
    return (
        min(rec1[2], rec2[2]) > # smallest right boundary
        max(rec1[0], rec2[0]) and # largest left boundary
        min(rec1[3], rec2[3] > # smallest top boundary
        max(rec1[1], rec2[1])) # largest bottom boundary
    )

'''
Minimum Time Visiting All Points

statement: you are given an array of n points with integer coordinates on a 2D plane, points, 
where points[i]=[xi,yi]; your task is to determine the minimum time in seconds required to visit 
all the points in the given order

movement rules:
- in one second, you can perform any one of the following:
    - move vertically by one unit
    - move horizontally by one unit
    - move diagonally (1 unit vertically and 1 unit horizontally in 1 second)
- you must visit the points in the exact sequence listed in the array
- you may pass through points that appear later in the order, but they will not count as visits

algorithm 
- iterate through consecutive points, calculating the absolute differences in their x and y 
  coordinates
- time to move between two points is the larger of these differences, as diagonal movement 
  optimizes travel
- x/y differences represent distances between 2 points on Cartesian plane 
- total time is the sum of these values for all pairs

time O(n) where n = total number of points in array, space O(1)
'''
def min_time_to_visit_all_points(points):   
    total_time = 0 
    n = len(points)
    
    # iterate through consecutive points in input list 
    for i in range(1, n):
        # calculate absolute difference in x and y coordinates for each pair 
        x_diff = abs(points[i][0] - points[i - 1][0])
        y_diff = abs(points[i][1] - points[i - 1][1])
        
        # determine movement time as maximum of x and y diffs and add movement time to running total 
        total_time += max(x_diff, y_diff)
    
    # return total time as min time to visit all points     
    return total_time

'''
Reverse Integer

statement: given a 32-bit signed integer num, reverse its digits and return the result; 
if the reversed number exceeds the 32-bit signed integer range 
[-2 ^ 31, 2 ^ 31 - 1], return 0 

assume the environment does not support storing 64-bit integers (signed or unsigned)

algorithm:
- reverse the digits of num while ensuring that the result stays within the bounds of a 
  32-bit signed integer
- if the input number is negative, it converts it to its absolute value to simplify 
  processing
- repeatedly extract the last digit of nums, reducing num by removing this digit, and 
  appending the digit to the reversed result
- before appending each digit, the solution checks if the operation would cause the 
  result to exceed the 32-bit signed integer limit
- if an overflow is detected, the function returns 0
- return the reversed result once the num is fully processed (reduced to 0)
- if the original number was negative, the result is negated before returning

'''

def reverse(num):
    # define max value for 32-bit signed integer 
    INT_MAX = 2 ** 31 - 1
    
    reversed_number = 0 
    
    # convert negative numbers to absolute 
    is_negative = num < 0   
    if is_negative:
        num = -num 
    
    # loop through digits until num becomes 0 
    while num != 0: 
        # extract last digit 
        digit = num % 10 
        
        # remove last digit from num 
        num //= 10 
        
        # check for overflow before updating result, return 0 for overflow 
        if reversed_number > (INT_MAX - digit) // 10:
            return 0 
        
        # update result by shifting previous digits and adding new 
        reversed_number = reversed_number * 10 + digit
    
    # return result with correct sign 
    return -reversed_number if is_negative else reversed_number

'''
Valid Square

statement: given the coordinates of four points P1, P2, P3 and P4 in 2D space, 
determine if these points form a square

each point Pi is represented as [xi,yi] and the points may be provided in any order

a square is defined as having:
    - four sides of equal positive length
    - four right angles (90 degrees)

algorithm: 
- utilize the fundamental geometric properties of a square 
- square: four equal sides and two equal diagonals 
- by calculating the distances between all pairs of points, we can classify these distances into side 
  lengths and diagonal lengths to verify the conditions of a square
- squared distance between two points, P1(x1,y1) and P2(x2,y2) is calculated using the formula below:
  
  (x2 - x1) ** 2  + (y2 - y1) ** 2 
    
- approach avoids the need for square roots, eliminating potential floating-point inaccuracies and 
  simplifying the comparison of distances
- by applying this formula to all six unique pairs of points, we obtain a set of squared distances that 
  can be analyzed to verify the properties of a square
- the six unique pairs of points are: (p1, p2), (p1, p3), (p1, p4), (p2, p3), (p2, p4), and (p3, p4)
- these pairs represent all possible combinations of two points among the four

time and space O(1)
'''
# helper function to calculate squared distance to avoid floating-point errors 
def distance_squared(point1, point2):
    return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 

def valid_square(p1, p2, p3, p4):
    # list all pairwise distances
    distances = [
        distance_squared(p1, p2),
        distance_squared(p1, p3), 
        distance_squared(p1, p4), 
        distance_squared(p2, p3), 
        distance_squared(p2, p4), 
        distance_squared(p3, p4)        
    ]
    
    distances.sort()

    # check properties of square 
    return (
    distances[0] > 0 and # checking that all side lengths are positive 
        distances[0] == distances[1] == distances[2] == distances[3] and # 1st 4 distances / side equal?  
        distances[4] == distances[5] # last 2 distances / diagonals equal? 
    )