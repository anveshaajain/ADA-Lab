# Quick Sort Algorithm (Step-by-Step)

# step 1: If the array has 0 or 1 elements, it is already sorted.

# step 2: Choose a pivot element from the array.

# step 3: Partition the remaining elements into two subarrays:

# step 4: elements smaller than or equal to the pivot

# step 6: elements greater than the pivot

# step 7: Recursively apply Quick Sort to the left and right subarrays.

# step 8: Combine the sorted left subarray, pivot, and sorted right subarray.

def Partition(arr, low, high):
    pivot = arr[low]
    i = low 
    j = high

    while i < j:
        while arr[i] <= pivot and i < high:
            i = i + 1
        while arr[i] > pivot:
            j = j - 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    arr[low], arr[j] = arr[j], arr[low]
    return j


def Quick_sort(arr, low, high):
    if low < high:
        pos = Partition(arr, low, high)
        Quick_sort(arr, low, pos - 1)
        Quick_sort(arr,pos + 1, high)


arr = [10,7,8,9,1,5]
Quick_sort(arr, 0, len(arr)-1)
print(arr)

