n = int(input("Enter the number of elements:"))
arr=list(map(int, input("enter the elements: ").split()))

for i in range(n-1):
    for j in range(n-i-1):
        if arr[j] > arr[ j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array is:", arr)