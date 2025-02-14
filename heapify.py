import heapq

def create_max_heap(arr):
    # Invert the sign of elements to use the min-heap as a max-heap
    max_heap = [-x for x in arr]
    heapq.heapify(max_heap)
    
    # To retrieve the max-heap elements, re-invert the values
    max_heap = [-x for x in max_heap]
    return max_heap

# Example usage
arr = [6, 15, 2, 4, 3, 8, 19]
max_heap = create_max_heap(arr)
print(max_heap)  # Output: [19, 15, 8, 4, 3, 6, 2]
