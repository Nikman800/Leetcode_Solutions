def countBalancedSubarrays(componentValue):

    # Initialize totalCount and difference to 0
    difference = 0
    total_count = 0
    
    # Initialize arrays to store frequency counts
    # Use length + 1 to handle potential maximum difference
    arr_size = len(componentValue)
    positive = [0] * (arr_size + 1)
    negative = [0] * (arr_size + 1)
    
    # Initial difference is 0, so positive[0] will be 1
    positive[0] = 1
    
    for num in componentValue:
        # Update difference based on whether number is odd or even
        if num % 2 == 0:  # even number
            difference -= 1
        else:  # odd number
            difference += 1
        
        # Handle negative and positive differences
        if difference < 0:
            # For negative differences, we look up in negative array
            # but need to use positive index
            abs_diff = abs(difference)
            total_count += negative[abs_diff]
            negative[abs_diff] += 1
        else:
            # For positive differences or zero, look up in positive array
            total_count += positive[difference]
            positive[difference] += 1
    
    return total_count



# Test cases
def run_tests():
    test_cases = [
        ([1, 2, 3, 4], 2),  # [1, 2, 3], [1]
        ([2, 4, 6], 0),     # No balanced subarrays
        ([1, 3, 5], 3),     # [1], [1, 3], [1, 3, 5]
        ([1, 2, 1, 2], 4)   # [1], [1, 2, 1], [1], [1, 2, 1]
    ]
    
    for arr, expected in test_cases:
        result = countBalancedSubarrays(arr)
        print(f"Array: {arr}")
        print(f"Expected: {expected}, Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}\n")

run_tests()