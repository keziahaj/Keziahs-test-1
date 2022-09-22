# A program that takes a list of numbers, and displays the average of the list, the biggest number and the midpoint.
# Keziah Ajufo
# 21/09/22

numbers_list = []

def validation():
    choice = int(input("How many numbers would you like to input? Please enter an amount above 2."))
    while choice < 3:
        print("Invalid input.")
        choice = int(input("How many numbers would you like to input? Please enter an amount above 2."))
    return choice
  
def numbers(choice, numbers_list):
    for x in range(choice):
        numbers = int(input(f"Enter up to" + (str(choice)) + "numbers please."))
        numbers_list = list(numbers)
        print(numbers_list)
    return numbers_list

def main(validation, numbers):
    print(numbers_list)

main()


