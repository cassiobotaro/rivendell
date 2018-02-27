def linear_search(list_, item):
    '''Searches for an item in linear way.

    Complexity: O(n)
    '''
    for index, value in enumerate(list_):
        if value == item:
            return index
    return None


def binary_search(list_, item):
    '''Searches for an item in a ordered list.

    Complexity: O(log(n))'''
    low = 0
    high = len(list_) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list_[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None
