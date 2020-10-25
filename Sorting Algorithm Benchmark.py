# This program is for comparing different sorting algorithm
from time import time
import random


def rand_arr(new_list):
    for k in range(25):
        n = random.randint(1, 100)
        new_list.append(n)
    return new_list

# selection sort


def selection_sort(arr):
    if len(arr) == 1:
        return arr
    n = len(arr)
    for j in range(10):
        for i in range(j, n):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

# bubble sort


def bubblesort(array):
    if len(array) == 1:
        return array
    n = len(array)
    for i in range(n):
        for k in range(n):
            k = k + 1
            if k < n:
                if array[k-1] > array[k]:
                    array[k-1], array[k] = array[k], array[k-1]
    return array

# merge sort


def mergesort(arr):
    if len(arr) == 1:
        return arr
    else:
        # divide the array in the midpoint length
        len_divider = len(arr)/2
        # Make recursive call to divide each side
        A = mergesort(arr[:len_divider])
        B = mergesort(arr[len_divider:])
        # Call merge function
        return merge(A, B)


def merge(A, B):
    # create pointer
    i = 0
    j = 0
    # final array
    results = []
    # while loop
    while i < len(A) and j < len(B):
        # check if A is less than B at select pointers, or else
        if A[i] < B[j]:
            results.append(A[i])
            i = i + 1
        else:
            results.append(B[j])
            j = j + 1
    # Add up the rest of the list
    if i == len(A):
        results = results + B[j:]
    else:
        results = results + A[i:]
    # Get results array
    return results

# main function call


def main():
    # create random array
    list1 = []
    list2 = []
    list3 = []
    list1 = rand_arr(list1)
    list2 = rand_arr(list2)
    list3 = rand_arr(list3)

    # merge sort function
    t0 = time()
    final_array = mergesort(list1)
    print('Sorted with merge :\n', final_array, '\n')
    t1 = time()
    print('%0.10f' % (t1-t0))

    # bubble sort function
    t2 = time()
    final_array_2 = bubblesort(list2)
    print('Sorted with bubble :\n', final_array_2, '\n')
    t3 = time()
    print('%0.10f' % (t3-t2))

    # selection sort function
    t4 = time()
    final_array_3 = selection_sort(list3)
    print('Sorted with selection :\n', final_array_3, '\n')
    t5 = time()
    print('%0.10f' % (t5-t4))


main()
