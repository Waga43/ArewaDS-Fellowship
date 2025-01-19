def welcome(name = "Arewa Data Science"):
    if name:
        print(f"Hello, {name}!")
    else:
        name = input("What is your name?\n")
        print(f"Hello, {name}!")

if __name__ == '__main__':
    welcome()