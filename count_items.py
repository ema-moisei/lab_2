""" 6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list
containing the items that appear exactly x times in the incoming lists.

Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4,
2 is in list 1 and 2, 3 is in lists 1 and 2."""


def compare_elements(list, counter):
    last_el = None
    nr_of_elements = 1
    item_list = []
    for element in list:
        if last_el is None:
            last_el = element
            continue
        if last_el == element:
            nr_of_elements += 1
            if nr_of_elements > counter:
                continue
        else:
            if nr_of_elements == counter:
                item_list.append(last_el)
            nr_of_elements = 1
            last_el = element
    if nr_of_elements == counter:
        item_list.append(last_el)
    return item_list


def count_items(counter, *lists):
    int_elements = []
    str_elements = []
    for list in lists:
        for element in list:
            if isinstance(element, str):
                str_element = list.pop(list.index(element))
                str_elements.append(str_element)
        int_elements.extend(list)

    str_elements.sort()
    int_elements.sort()

    item_list_int = compare_elements(int_elements, counter)
    item_list_str = compare_elements(str_elements, counter)
    item_list_int.extend(item_list_str)
    print(item_list_int)


def main():
    list1 = [1, 2, 1, 3, "text", 8]
    list2 = [1, 4, 5, "a", 6, "b"]
    list3 = [3, 7, 88, "a", 6, "b"]
    list4 = [7, 7, 8, 103, 9, "b"]
    x = 1
    count_items(x, list1, list2, list3, list4)


if __name__ == "__main__":
    main()
