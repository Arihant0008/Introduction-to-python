# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not a integer")

# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not a integer")
# else:
#     print(f"x is {x}")

# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not a integer")
#     else:
#         break

# print(f"x is {x}")

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            pass
main()