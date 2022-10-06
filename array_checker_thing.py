# A program that takes a list of numbers, and displays the average of the list, the biggest number and the midpoint.
# Keziah Ajufo
# 21/09/22


average = 0 

def validation():
    choice = int(input("How many numbers would you like to input? Please enter an amount above 2."))
    while choice < 3:
        print("Invalid input.")
        choice = int(input("How many numbers would you like to input? Please enter an amount above 2."))
    return choice
  

def numbers(choice):
    num_list = []
    for x in range(choice):
        inpt = input(f" Enter number {x+1}")
        num_list.append(inpt)
    print(num_list)


def sum(num_list):
    sum = 0
    for x in range(0,len(num_list)):
        sum = sum + num_list[x]
        print("Sum of all your numbers.")

def display(sum, num_list):

    average = (sum/len(num_list))
    print(average)
    
    largest_number = num_list[0]
    for x in num_list:
        if x > largest_number:
            largest_number = x
            print(largest_number)

    midpoint = (sum + 1)/2
    print(midpoint)

output = validation()
numbers(choice)
print(validation())
sum(num_list)






        
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





