# step 1: start 
# step 2: Read n 
# step 3: Read array elements 
# step 4: Set max = first element of an array 
# step 5: comapre eachelement with max and update if any large element found 
# step 6: print max 
# step 7: stop

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))
    
maximum = arr[0]

for i in range(1, n):
    if arr[i] > maximum:
        maximum = arr[i]
        
print("maximum element in the array is: ", maximum)    
    