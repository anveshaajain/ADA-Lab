def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        mid_index = i
        for j in range(i+1,n):
            if arr[j] < arr[mid_index]:
                mid_index = j
        arr[i], arr[mid_index] = arr[mid_index], arr[i]
    return arr

arr= [20, 40,30,10,60,0]
print(selection_sort(arr))

    