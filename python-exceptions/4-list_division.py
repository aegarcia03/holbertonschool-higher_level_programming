#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list_3 = []

    for i in range(list_length):
        try:
            list_3.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            list_3.append(0)
            print("division by 0")
            continue
        except TypeError:
            list_3.append(0)
            print("wrong type")
            continue
        except IndexError:
            list_3.append(0)
            print("out of range")
        finally:
            pass

    return list_3
