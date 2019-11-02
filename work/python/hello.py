first_name = input("What is your first name? ")
print("Hello,", first_name)
if first_name == "Steve":
    print(first_name, "is Learning Python")
elif first_name == "Maximiliane":
    print(first_name, "is learning with fellow students in the community! Me too!")
else:
    # This is just in case we have a younger user
    age = int(input("How old are you? "))
    if age <= 6:
        print("WOW you're {}! If you're confident with your reading already...".format(age))
    print("You should totally learn Python, {}!".format(first_name))
print("have a great day {}:".format(first_name))

# I am a python code comment. Above you will see python indents these are called decision braches and this is a decision tree.

