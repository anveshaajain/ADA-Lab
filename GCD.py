def gcd(a, b):
    while b!=0:
        a,b= b, a % b
    return a 

num1= 10
num2= 20

print("GCD is: ", gcd(num1, num2))    