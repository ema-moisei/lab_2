"""1. Write a function to return a list of the first n numbers in the Fibonacci string."""


def fibonacci(number):
    """Calculates each term of the Fibonacci series and assigns the values one by one to a string"""
    F0 = 0
    if number == 1:
        fibonacci_string = "0"
    elif number == 2:
        fibonacci_string = "0, 1"
    else:
        Fn = 1
        fibonacci_string = "0, 1"
        while number > 2:
            Fn, F0 = Fn + F0, Fn
            number -= 1
            fibonacci_string += ", " + str(Fn)
    return fibonacci_string


def ask_for_input():
    """Ask the user for a number"""
    number = 0
    while number < 1:
        number = int(input("How many numbers do you want to be displayed from the Fibonacci sequence?: "))
        if number < 1:
            print("Please enter a number bigger or equal to 1")
    return number


def main():

    print(fibonacci(ask_for_input()))


if __name__ == "__main__":
    main()
