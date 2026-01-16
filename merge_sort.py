# Algorithm : Merge Sort\
# step 1 : start 
# step 2 : read array A with n elements
# step 3 : if n <= 1 , return A
# step 4 : find middle index mid = n/2
# step 5 : Diuvide array into 
#          Left subarray L = A[0 _____ mid - 1]
#          Right subarray R = A[mid _____ n - 1]
# step 6 : Apply Merge sort on L
# step 7 : Apply Merge sort on R 
# step 8 : Merge L and R into sorted array A 
#          * compare elements from L and R 
#          * insert smaller elements into A
#          * copy remaining elments 
# step 9 : return sorted array A 
# step 10 : stop 


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    L = arr[:mid]
    R = arr[mid:]
    
    L = merge_sort(L)
    R = merge_sort(R)
    
    i = j = 0
    result = []
    
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i += 1
        else:
            result.append(R[j])
            j += 1
            
    result.extend(L[i:])
    result.extend(R[j:])
    
    return result


arr = []
n = int(input("Enter number of elements in the array: "))
for i in range(n):
    arr.append(int(input("Enter the array elements: ")))
sorted_arr = merge_sort(arr)
print("Sorted array is:", sorted_arr)

