# A program that takes a list of numbers, and displays the average of the list, the biggest number and the midpoint.
# Keziah Ajufo
# 21/09/22


# from secrets import choice


def validation():
    choice = 0
    while choice < 3:
        print("Invalid input.")
        choice = int(input("How many numbers would you like to input? Please enter an amount above 2."))
    return choice
  

def numbers(output):
    num_list = []
    total = 0
    for x in range(output):
        inpt = int(input(f" Enter number {x+1}"))
        num_list.append(inpt)
    
    total = sum(num_list)
    print(f'The total is {total}')

    return num_list, total 


def display(num_list, total):

    average = 0
    average = (total/len(num_list))
    print(f'The average is {round(average, 2)}')
    
    largest_number = num_list[0]
    for x in num_list:
        if x > largest_number:
            largest_number = x
    
    print(f'The largest number is {largest_number}')

    
    midpoint = (total)/2
    print(f'The total midpoint is {midpoint}')

output = validation()
num_list, total = numbers(output)
display(num_list, total)


   

    
# numbers_list = list(numbers)
# numbers_list(output)
# print(numbers_list)
  #  return numbers_list

 # A program that identifies if a number is even or odd

def identifier():
    number1 = int(input("Enter a number."))
    calc = number1/2

    if calc == int:
        print(f" {number1} is an even number.")
    else:
        print(f"{number1} is an odd number")

identifier()

# function that asks for a person name and separates the name into letters in a list
# learn the common methods used in a list

def name():
    name = input(f'What is your name?')
    list = []

    for x in name:
        list.append(x)

    print(list)

name()

# create a program that identifies if a number is odd or even (same as the one, two above)

def num():
    
    num = int(input("Enter a number"))
    if (num % 2) == 0:
        print(f'{num} is an even number.')
    else:
        print(f'{num} is an odd number.')

num()




