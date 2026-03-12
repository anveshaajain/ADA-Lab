# step 1: start
# step 2: read n
# step 3: read the sorted array elements
# step 4: read the element [key] to be searched
# step 5: set low = 0, high = n-1
# step 6: while low <= high 
#         mid = (low + high) // 2
#         if arr[mid] == key
#             print "element found at position mid + 1"
#             stop
#         else if arr[mid] < key
#             low = mid + 1
#         else
#             high = mid - 1
# step 7: if element not found, print "element not found"
# step 8: stop

arr = []
n = int(input("Enter number of elements in the sorted array: "))

for i in range(n):
    arr.append(int(input("Enter the array elements: ")))
    
key = int(input("Enter the element to be searched: "))

low = 0
high = n-1 
found = False

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == key:
        print(f"Element found at the position {mid + 1}")
        found = True 
        break
    elif arr[mid] < key:
        low = mid + 1
    else:
        high = mid - 1
        
if not found:
    print("Element not found in the array!!!")
    