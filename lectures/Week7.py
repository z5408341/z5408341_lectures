import copy

import pprint as pp

def printit(obj, msg):

    sep = '-' * 30
    to_print = [
        sep,
        msg,
        '',
        pp.pformat(obj),
        '',
        f"Type: {type(obj)}",
        f"Object Address: {id(obj)}",
        sep,
        ]
    print('\n'.join(to_print))


def example1():

    lst0 = [1, 2]


    printit(lst0, "EXAMPLE 1: This is lst0")


    lst1 = [1, 2]


    printit(lst1, "EXAMPLE 1: This is lst1")


def example2():

    lst0 = [1, 2]
    lst1 = [1, 2]

    lst2 = lst0

    printit(lst0, "EXAMPLE 2: This is lst0")
    printit(lst1, "EXAMPLE 2: This is lst1")
    printit(lst2, "EXAMPLE 2: This is lst2")


def example3():

    lst0 = [1, 2]
    lst1 = [1, 2]

    lst2 = lst0

    printit(lst0, "EXAMPLE 3: This is the ORIGINAL lst0")
    printit(lst1, "EXAMPLE 3: This is the ORIGINAL lst1")
    printit(lst2, "EXAMPLE 3: This is the ORIGINAL lst2")

    lst2[0] = -99



    printit(lst0, "EXAMPLE 3: This is lst0 after setting lst2[0] = -99")
    printit(lst1, "EXAMPLE 3: This is lst1 after setting lst2[0] = -99")
    printit(lst2, "EXAMPLE 3: This is lst2 after setting lst2[0] = -99")


def example4():

    lst0 = [1, 2]
    lst1 = [3, [1, 2]]


    printit(lst0, "EXAMPLE 4: This is lst0 (single list)")
    printit(lst1, "EXAMPLE 4: This is lst1 (nested lists, the ID is for the outer list)")
    printit(lst1[1], "EXAMPLE 4: This is lst1[1] (the inner list)")


def example5():

    lst0 = [1, 2]
    lst1 = [3, [1, 2]]
    lst2 = [3, lst0]


    printit(lst0, "EXAMPLE 5: This is lst0 (single list)")
    printit(lst1, "EXAMPLE 5: This is lst1 (nested lists, the ID is for the outer list)")
    printit(lst1[1], "EXAMPLE 5: This is lst1[1] (the inner list)")
    printit(lst2, "EXAMPLE 5: This is lst2 (the outer list)")
    printit(lst2[1], "EXAMPLE 5: This is lst2[1] (the same list as lst0)")


def example6():

    lst0 = [1, 2]


    lst1 = copy.copy(lst0)


    printit(lst0, "EXAMPLE 6: This is lst0")
    printit(lst1, "EXAMPLE 6: This is lst1")


def example7():

    lst0 = [1, 2]
    lst1 = [3, lst0]
    lst2 = copy.copy(lst1)


    printit(lst0, "EXAMPLE 7: This is lst0")
    printit(lst1, "EXAMPLE 7: This is lst1")
    printit(lst2, "EXAMPLE 7: This is lst2")


    printit(lst0, "EXAMPLE 7: This is lst0 (again)")
    printit(lst1[1], "EXAMPLE 7: This is lst1[1]")
    printit(lst2[1], "EXAMPLE 7: This is lst2[1]")


    lst3 = copy.deepcopy(lst1)

    printit(lst0, "EXAMPLE 7: This is lst0 (again)")
    printit(lst3[1], "EXAMPLE 7: This is lst3[1] (different than lst0)")


def main():
    """
    """


if __name__ == "__main__":
    main()