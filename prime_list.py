"""2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it."""
from math import *


def prime_number(number):
    """Check if a number is prime"""
    number = int(number)
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    rad = int(sqrt(number))
    for divisor in range(3, rad + 1, 2):
        if number % divisor == 0:
            return False
    return True


def list_of_the_prime_numbers(list):
    """Returns a list of the prime numbers found in given list"""
    prime_list = []
    for element in list:
        if prime_number(element):
            if element not in prime_list:
                prime_list.append(element)
    print(prime_list)


def ask_for_input():
    """Ask the user for input"""
    list = []
    number = 1
    print("Enter the numbers you want to check and when you are done enter \"ok\":")
    while number != "ok":
        number = input()
        if number.isdigit():
            list.append(number)
    return list


def main():
    list = ask_for_input()
    list_of_the_prime_numbers(list)


if __name__ == "__main__":
    main()
