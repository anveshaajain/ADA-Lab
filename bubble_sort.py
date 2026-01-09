# step 1:Start
# step 2: Read n
# step 3: Read n elements into array A[0…n−1]
# step 4: Repeat for i = 0 to n−2
# step 5: Repeat for j = 0 to n−i−2
# step 6: If A[j] > A[j+1], swap A[j] and A[j+1]
# step 7: After all passes, the array is sorted
# step 8: Print the sorted array
# step 9: Stop

arr =[]
n = int(input("Enter number of elements in the array: "))
for i in range(n):
    arr.append(int(input("Enter the array elements: ")))
    
for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            
print("Sorted array is: ")
for i in range(n):
    print(arr[i], end=" ")
    