# Ask user for their name
name = input("What's your name? ").strip().title()


# # Remove whitespace from str and capatilize users name
# name = name.strip().title()

# #Capitalize user's name
# # name = name.capitalize()
# name = name.title()

# Split's user's name into first name and last name
first, last = name.split(" ")
# Say hello to user
# print("hello, ", name, sep= "")   # can also use ' + ' for concatination also sep, end -> for line ending
# print(name)

print(f"hello, {first}")



