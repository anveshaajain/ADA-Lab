# Merge Sort Algorithm

# Step 1: Start

# Step 2: Read the number of elements n

# Step 3: Read the elements of the array

# Step 4: Find the middle position of the array

# Step 5: Divide the array into two subarrays: left and right

# Step 6: Repeat the division process until each subarray contains only one element

# Step 7: Merge the subarrays by comparing elements from the left and right arrays

# Step 8: Place the smaller element first, followed by the larger element

# Step 9: Continue merging until the entire array is sorted

# Step 10: Print the sorted array



def Merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = Merge_sort(arr[:mid])
    right = Merge_sort(arr[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


arr = list(map(int, input().split()))
sorted_arr = Merge_sort(arr)
print(sorted_arr)