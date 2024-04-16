def insertion_sort(array):
    """
    Sort the array using the Insertion sort algorithm

    Parameters:
    - array: The array to be sorted

    Returns: Nothing. The array is sorted in-place.
    """
    for i in range(1, len(array)):
        key_index = i
        for j in range(key_index):
            if array[j] > array[key_index]:
                array[key_index], array[j] = array[j], array[key_index]


array = [6, 8, 5, 1, 2]
insertion_sort(array)
print(array)


#def insertion_sort(array):
#    """
#    Sort the array using the Insertion sort algorithm
#
#    Parameters:
#    - array: The array to be sorted
#
#    Returns: Nothing. The array is sorted in-place.
#    """
#    for i in range(1, len(array)):
#        key_index = i
#        for j in range(i):
#            if array[j] > array[key_index]:
#                array[key_index], array[j] = array[j], array[key_index]
#                break  # Break after finding the correct position
#
#array = [6, 8, 5, 1, 2]
#insertion_sort(array)
#print(array)
#