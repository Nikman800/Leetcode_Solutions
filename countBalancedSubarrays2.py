def count_balanced_subarrays(arr):
    from collections import defaultdict
    # Dictionary to count prefix states.
    # The state is (even_parity, odd_parity)
    prefix_count = defaultdict(int)
    # Initialize with the empty prefix state (0 evens, 0 odds)
    prefix_count[(0, 0)] = 1

    even_parity = 0  # parity of even count so far (0 means even count)
    odd_parity = 0   # parity of odd count so far (0 means even count)
    result = 0

    for num in arr:
        if num % 2 == 0:
            even_parity ^= 1  # Flip even parity bit if even number found.
        else:
            odd_parity ^= 1   # Flip odd parity bit if odd number found.

        # Current state after including num.
        current_state = (even_parity, odd_parity)
        # To have a balanced subarray ending at current index,
        # the prefix state before the subarray must have:
        #   same even parity, and opposite odd parity.
        target_state = (even_parity, 1 - odd_parity)
        result += prefix_count[target_state]

        # Record the current state for future subarrays.
        prefix_count[current_state] += 1

    return result


# Test cases
def test():
    test_cases = [
        ([1], 1),
        ([3], 1),
        ([2], 0),
        ([1, 2, 3, 4], 3),  # Valid subarrays: [1], [3], [2,3,4]
        ([1, 3, 5], 4),     # Valid: [1], [3], [5], [1,3,5]
        ([2, 4, 6], 0),     # No valid subarrays
        ([1, 2, 1, 2], 3),   # Valid: [1], [2,1,2], [1]
        ([1, 2, 3, 4, 5], 5)
    ]
    
    for arr, expected in test_cases:
        result = count_balanced_subarrays(arr)
        print(f"Input: {arr}")
        print(f"Expected: {expected}, Got: {result}")
        print("Test", "passed" if result == expected else "failed", "\n")

test()