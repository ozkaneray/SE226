Sn = 0

def calculate(n, current=1):

    global Sn
    if current > n:
        return
    Sn += (-1) ** (current + 1) * (1 / current)
    calculate(n, current + 1)

n = int(input("Enter n: "))
calculate(n)
print(f"S{n} = {Sn}")
