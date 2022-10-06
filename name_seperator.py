# function that asks for a person name and separates the name into letters in a list
# learn the common methods used in a list

def name():
    name = input(f'What is your name?')
    list = []

    for x in name:
        list.append(x)

    print(list)

name()
