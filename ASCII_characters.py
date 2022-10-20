"""8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to
True. For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is
set to True, otherwise it should contain characters that have the ASCII code not divisible by x.

 Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" . Note: The function must
 return list of lists."""


def ASCII_characters(list, x=2, flag=True):
    final_list = []
    for element in list:
        character_list = []
        if flag:
            for char in element:
                if ord(char) % x == 0:
                    character_list.append(char)
            final_list.append(character_list)
        else:
            for char in element:
                if ord(char) % x != 0:
                    character_list.append(char)
            final_list.append(character_list)
    return final_list


def main():

    list = ["test", "hello", "lab002"]
    characters = ASCII_characters(list, 2, False)
    print(characters)


if __name__ == "__main__":
    main()
