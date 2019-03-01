

def bubbleSort(arr):
    '''
    It compares adjacent items and exchanges those that are out of order.
    Each pass through the list places the next largest value in its proper place.
    In essence, each item “bubbles” up to the location where it belongs.
    :param arr: list to be sorted
    :return: sorted list
    '''
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

def selectionSort(arr):
    '''
     A selection sort looks for the largest value as it makes a pass and, after completing the pass, places it in the proper location.
     As with a bubble sort, after the first pass, the largest item is in the correct place, but makes fewer swaps
    :param arr: array to be sorted
    :return: sorted array
    '''
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index], arr[i]

    return arr

def insertionSort(arr):
    '''
    Insertion sort uses a subarray which is sorted
    uses a variable item to keep store of current index element
    :param arr: array to be sorted
    :return: sorted array
    '''
    for i in range(1, len(arr)):
        item = arr[i]
        j = i-1

        while(j>=0 and arr[j]>item):
            arr[j+1] = arr[j]
            j-=1

        arr[j+1] = item
    return arr





a = [5,4,9,20,12, 1, 1090, 100, 123, 22, 9]
print("\nOriginal Array -> " + str(a))


sorted_arr = insertionSort(a)


print("\nSorted Array -> "+ str(sorted_arr))


