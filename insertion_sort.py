# Python program for implementation of Insertion Sort
# Acknowledgement: InteractivePython


def insertion_sort(alist):

    # Traverse through list elements, from second value in list to the last position
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index

        # Determines whether index value (a) in list is less than index values preceding it.
        # If true, move all greater values up one position in list
        # Insert initial index value (a) when index a-1 < a or beginning of list (index 0) is reached.
        while position > 0 and alist[position - 1] < current_value:
            alist[position] = alist[position - 1]
            position = position - 1
            print(alist)
        alist[position] = current_value


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]


insertion_sort(alist)
print(alist)
