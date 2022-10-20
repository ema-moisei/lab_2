"""7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
The first element of the tuple will be the number of palindrome numbers found in the list and the second element will
be the greatest palindrome number."""


def check_palindrome(list):
    largest_palindrome_chr = 0
    largest_palindrome = ""
    palindrome_nr = 0
    for number in list:
        palindrome = True
        element = str(number)
        for first_nr in element[:len(element) // 2]:
            index = element.index(first_nr)
            last_nr = element[(len(element) - 1) - index]
            if not first_nr == last_nr:
                palindrome = False
                break
        if palindrome:
            palindrome_nr += 1
            if len(element) > largest_palindrome_chr:
                largest_palindrome_chr = len(element)
                largest_palindrome = element
    return palindrome_nr, largest_palindrome


def main():

    list = [35953, 1, 45, 7842, 121, 12321, 54, 789, 415, 123454321]
    palindrome_nr, largest_palindrome = check_palindrome(list)
    print(palindrome_nr, int(largest_palindrome))


if __name__ == "__main__":
    main()
