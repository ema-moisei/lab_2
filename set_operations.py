"""3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited
with b, a - b, b - a)"""
# e ok sa folosesc set?

def set_operations(list1, list2):
    intersection = [element for element in list1 if element in list2]
    aux_list = list(list1)
    aux_list.extend(list2)
    reunited = list(set(aux_list))
    list1_list2 = [element for element in list1 if element not in list2]
    list2_list1 = [element for element in list2 if element not in list1]
    print("a intersected with b is:", intersection)
    print("a reunited with b is: ", reunited)
    print("a - b is: ", list1_list2)
    print("b - a is: ", list2_list1)


def main():

    list1 = [10, 15, 20, 25, 30, 35, 40]
    list2 = [25, 35, 40, 50, 88]
    set_operations(list1, list2)


if __name__ == "__main__":
    main()
