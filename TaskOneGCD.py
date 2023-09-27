
from typing import List



# i made this function to check the numbers and drop an error if the number is negative
def get_positive_int(promot= "Enter a positive integer: "):

    while True:
        try:
            user_input = int(input(promot))
            if user_input > 0:
                return user_input
            else:
                print("positive interger Only")
        except ValueError:
            print("Wrong input, just positive interger: ")



# this function to make a list with valid numbers
def get_numbers() -> List[int]:

    print("enter the lenght of your List")
    list_lenght = get_positive_int()     # define the lenght of the list, it must be positive and greater than ZERO

    my_list_1 = []  # define the empty list 

    for i in range(list_lenght):

        print("[", i + 1, "]") # step number
        user_input = get_positive_int()
        my_list_1.append(user_input)
    
    return my_list_1



# first function   gcd_two_numbers(a: int, b: int)
def gcd_two_numbers(a: int, b: int) -> int:


    while b != 0:
        a ,b = b, a % b

    return a

# this function is for finding the gcd of list
def gcd_numbers(my_list: List[int]) -> int:

    for num in my_list:
        if num <= 0:
            raise ValueError("Invalid input. Please provide a list of positive integers.")
    
    result = my_list[0]
    for num in my_list[1:]:
        result = gcd_two_numbers(result, num)
    
    return result




# here I'm asking the user to enter TWO numbers to get the GCD
print("Here the program will ask you to enter 2 positive numbers, then the program will give you the GCD of them\n")

number_1 = get_positive_int()  # here I use """user get_positive_int()""" to only get positive number and greater then 0
number_2 = get_positive_int()
gcd_of_tow = gcd_two_numbers(number_1, number_2)
print("the GCD of the numbers you wrote is: ", gcd_of_tow)



print("\n\nNow the program will ask you to make a list, first you should define the lenght of your list, then the program will give the the GCD of your list\n***make sure that all the numbers are positive\n\n")

final_list = get_numbers()  # here i make the list  
gcd_of_list = gcd_numbers(final_list)
print("\nyour List\n", final_list)

print("the GCD of your List:  ",gcd_of_list)







          