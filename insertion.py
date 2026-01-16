# Algorith : Insertion Sort
# step 1 : start
# step 2 : read array A with n elements
# step 3 : for i = 1 to n-1 do
#          set key = A[i]
#          set j = i - 1
# step 4 : while j >= 0 and A[j] > key
#          move A[j] one position to the right
#          decrease j by 1 
# step 5 : insert key at position j + 1
# step 6 : repeat steps 3-5 until array is sorted
# step 7 : stop

def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            
        arr[j + 1] = key
        
    return arr


arr = []
n = int(input("Enter number of elements in the array: "))       
for i in range(n):
    arr.append(int(input("Enter the array elements: ")))
sorted_arr = insertion_sort(arr)
print("Sorted array is:", sorted_arr)

