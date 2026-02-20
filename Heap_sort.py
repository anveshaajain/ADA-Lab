# Algorithm 
# step 1: Start 
# step 2: Read number of elments n 
# step 3: Build a max heap 
#         * set i =[n/2] -1 
#         * Repeat until i >= 0
#         * call Max-Heapify(A,n,i)
#         * decrement i by 1
# step 4: Perdorm heap sort 
#         * Set i = n-1
#         * Repeat until i > 0
#         * swap A[0] and A[i]
#         * call Max-Heapify(A,i,0)
#         * decrement i by 1
# step 5: Stop

#  Algorithm: MAX-HEAPIFY(A, n, i)
# Step 1: Set largest = i

# Step 2: Set left = 2*i + 1

# Step 3: Set right = 2*i + 2

# Step 4: If left < n and A[left] > A[largest], set largest = left

# Step 5: If right < n and A[right] > A[largest], set largest = right

# Step 6: If largest ≠ i

# Swap A[i] and A[largest]

# Call MAX-HEAPIFY(A, n, largest)

# Step 7: Return

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements separated by space: ").split()))

heap_sort(arr)

print("Sorted array:", arr)