# step 1: start 
# step 2: read n
# step 3: read the array elements
# step 4: read the element [key] to be searched
# step 5: set i = 0 
# step 6: repeat while i < n
#         if arr[i] == key
#         print "element found in the position i + 1"
#         stop
#         else
#         increase i by 1
# step 7: if i =n, print "element not found"
#step 8: stop 

arr = []
n = int(input("Enter number of elements in the array: "))

for i in range(n):
    arr.append(int(input("Enter the array elements: ")))
    
key = int(input("Enter the element to be searched: "))

found = False

for i in range(n):
    if arr[i] == key:
        print(f"Element found at the position {i + 1}")
        found = True
        break
    
if not found:
    print("Element not found in the array!!!")   
      