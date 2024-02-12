#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """
        Divide element by element of 2 list
    """

    result = []  # To hold quotients of division operation

    for index in range(list_length):
        try:
            quotient = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            quotient = 0
            print("division by 0")
        except TypeError:
            quotient = 0
            print("wrong type")
        except IndexError:
            quotient = 0
            print("out of range")
        finally:
            result.append(quotient)

    return result
