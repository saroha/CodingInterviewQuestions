# Given a rotated sorted array, find the index of second input value - in minimum possible time complexity

# Find index of k in input_array
input_array = [4, 5, 6, 7, 8, 9, 1, 2, 3]
k = 3


# Step 1 - Find the element index which splits input into 2 sorted arrays, 1 in our case
def find_pivot(beg, end, array):
    mid = (end + beg) // 2
    if array[beg] < array[end]:
        return -1
    if array[mid] < array[mid - 1]:
        return mid
    if array[beg] > array[mid]:
        return find_pivot(beg, mid, array)
    if array[end] < array[mid]:
        return find_pivot(mid, end, array)


def binary_search(beg, end, array, k):
    mid = (beg + end) // 2
    if k == array[mid]:
        return mid
    if beg >= end:
        return -1
    else:
        if k > array[mid]:
            return binary_search(mid + 1, end, array, k)
        else:
            return binary_search(beg, mid - 1, array, k)


# Identify pivot element
pivot = find_pivot(0, len(input_array) - 1, input_array)

if pivot == -1:
    # List is Linear sorted
    print(binary_search(0, len(input_array) - 1, input_array, k))
else:
    if input_array[0] <= k <= input_array[pivot - 1]:
        # Element would lie in left sub-array
        print(binary_search(0, pivot - 1, input_array, k))
    else:
        print(binary_search(pivot, len(input_array), input_array, k))
        # Element would lie in right sub-array
