def sort_four_nums(num1, num2, num3, num4):
    
    # round 1
    min_round_1 = min(num1, num2)
    max_round_1 = max(num1, num2)
    
    # round 2
    smallest = min(min_round_1, num3, num4)
    temp_max = max(min_round_1, num3, num4)
    temp_middle = min_round_1 + num3 + num4 - smallest - temp_max
    
    # round 3
    largest = max(max_round_1, temp_max, temp_middle)
    second_smallest = min(max_round_1, temp_max, temp_middle)
    second_largest = max_round_1 + temp_max + temp_middle - second_smallest - largest
    
    
    # final
    
    print(smallest, second_smallest, second_largest,largest)
