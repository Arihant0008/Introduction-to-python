name = input("What's your name? ")

# if name == "Harry":
#     print("Grffindor")
# elif name == "Hermione":
#     print("Grffindor")
# elif name == "Ron":
#     print("Grffindor")
# elif name == "Draco":
#     print("Grffindor")
# else:
#     print("Who?")

# if name == "Harry" or name == "Hermione" or  name == "Ron" or name == "Draco":
#     print("Grffindor")
# else:
#     print("Who?")

# match name:
#     case "Harry":
#         print("Grffindor")
#     case "Hermione":
#         print("Grffindor")
#     case  "Draco":
#         print("Slytherin")
#     case _:
#         print("Who? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Grffindor")
    case  "Draco":
        print("Slytherin")
    case _:
        print("Who? ")
