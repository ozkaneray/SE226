def factorial(x):
    if x<0:
        ValueError("Factorial can only take positive integers")
    if x==0 or x==1:
        return 1
    return x*factorial(x-1)

print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(4))
print(factorial(5))

term = lambda x, n: (x ** n) / factorial(n)

def exp (x, n):
    result = 0
    for i in range(n):
        result += term(x, i)
    return result

x = float(input("Enter x: "))
n = int(input("Enter number of terms (n): "))

print(f"e^{x} ≈ {exp (x, n)}")
