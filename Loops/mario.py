# for _ in range(3):
#     print("#")

# def main():
#     print_column(3)

# def print_column(height):
#     print("#\n" * height, end="")
# main()

# def main():
#     print_row(4)

# def print_row(height):
#     print("?" * height)
# main()

def main():
    square(3)

def square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print("#", end="")

        print()
main()

# def main():
#     square(3)

# def square(size):
#     for i in range(size):
#         print("#" * size)
# main()

# def main():
#     print_square(3)

# def print_square(size):
#     for i in range(size):
#         print_row(size)

# def print_row(width):
#     print("#" * width)

# main()