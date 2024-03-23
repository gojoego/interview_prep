def intervals_intersection(interval_list_a, interval_list_b):
    intersections = []
    i = j = 0
    
    while i < len(interval_list_a) and j < len(interval_list_b):
        start = max(interval_list_a[i][0], interval_list_b[j][0])
        end = min(interval_list_a[i][1], interval_list_b[j][1])
        
        if start <= end:
            intersections.append([start, end])
            
        if interval_list_a[i][1] < interval_list_b[j][1]:
            i += 1
        else:
            j += 1
    
    return intersections

def main():
    input_interval_list_a = [
        [[1, 2]],
        [[1, 4], [5, 6], [9, 15]],
        [[3, 6], [8, 16], [17, 25]],
        [
            [4, 7],
            [9, 16],
            [17, 28],
            [39, 50],
            [55, 66],
            [70, 89],
        ],
        [
            [1, 3],
            [5, 6],
            [7, 8],
            [12, 15],
        ],
    ]
    input_interval_list_b = [
        [[1, 2]],
        [[2, 4], [5, 7], [9, 15]],
        [[2, 3], [10, 15], [18, 23]],
        [
            [3, 6],
            [7, 8],
            [9, 10],
            [14, 19],
            [23, 33],
            [35, 40],
            [45, 59],
            [60, 64],
            [68, 76],
        ],
        [[2, 4], [7, 10]],
    ]

    for i in range(len(input_interval_list_a)):
        print(i + 1, '.\t Interval List A: ', input_interval_list_a[i], sep="")
        print('\t Interval List B: ', input_interval_list_b[i], sep="")
        print("\t Intersecting intervals in 'A' and 'B' are: ", intervals_intersection(input_interval_list_a[i], input_interval_list_b[i]), sep="")

        print('-' * 100)


if __name__ == "__main__":
    main()