x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
z = round(x + y,2)
print(f"{z:.2f}")
print(f"{z:,}")

def main():
    x = int(input("Enter the value of x: "))
    print("x squared is", square(x))

def square(n):
    # return n * n
    # return n ** 2
    return pow(n, 2)

main()