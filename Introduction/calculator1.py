def main():
    x = int(input("What's x? "))
    print("x is squared is", square(x))

def square(n):
    return n * n    # n**2 or pow(n, 2)

main()