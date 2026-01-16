# Step 1: Start

# Step 2: Read array A with n elements

# Step 3: For i = 0 to n − 2

# Assume the minimum element index is i

# Step 4: For j = i + 1 to n − 1

# If A[j] < A[min_index], set min_index = j

# Step 5: Swap A[i] and A[min_index]

# Step 6: Repeat Steps 3–5 until array is sorted

# Step 7: Stop

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = []
n = int(input("Enter number of elements in the array: "))
for i in range(n):
    arr.append(int(input("Enter the array elements: ")))
sorted_arr = selection_sort(arr)
print("Sorted array is:", sorted_arr)
