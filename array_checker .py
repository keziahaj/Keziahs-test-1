# A program that takes a list of numbers, and displays the average of the list, the biggest number and the midpoint.
# Keziah Ajufo
# 21/09/22

numbers_list = []
average = 0 

def main():
    print(numbers_list)

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



def display():

    average = (numbers_list/len(numbers_list))
    print(average)
    
    largest_number = numbers_list[0]
    for x in numbers_list:
        if x > largest_number:
            largest_number = x
            print(largest_number)

    midpoint = (numbers_list + 1)/2
    print(midpoint)

main()

 
 # A program that identifies if a number is even or odd

number1 = int(input("Enter a number."))
calc = number1/2

if calc == int:
    print(number1 + f"is an even number.")
else:
    print(number1 + f"is an odd number")





