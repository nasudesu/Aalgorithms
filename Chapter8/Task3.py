def binary_search_iterative(array, value):
    """
    Performs a binary search in the the array for the given value

    Parameters:
    - array: The array where to perform the search
    - value: The value being searched

    Returns: The index of the value if it is found.
             Or None if it is not found.
    """
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == value:
            return middle
        if value > array[middle]:
            left = middle + 1
        if value < array[middle]:
            right = middle - 1
    return "Numero ei löydy"


array = [1, 3, 4, 5, 6, 7, 8, 9, 10]
print(binary_search_iterative(array, 2))
