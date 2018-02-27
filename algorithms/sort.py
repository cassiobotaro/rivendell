def find_smallest(arr):
    'Given a iterable, returns smallest index.'
    smallest, *_ = arr
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    '''Order an iterable using selection sort.

    Complexity: O(n²)
    '''
    ordered = []
    for _ in range(len(arr)):
        smallest = find_smallest(arr)
        ordered.append(arr.pop(smallest))
    return ordered
