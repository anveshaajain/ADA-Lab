# step 1: start 
# step 2: enter integer 
# step 3: (using recursive) If n = 0 or 1, return 1
# step 4: otherwise, return n*factorial(n-1)
# step 5: stop 

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1) 
    
num = 5
print(f"factorial of {num} is {fact(num)}")    