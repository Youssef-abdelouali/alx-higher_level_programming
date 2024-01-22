#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    _newList_ = []
    for i in range(0, list_length):
        try:
            _divis_ = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            _divis_ = 0
        except ZeroDivisionError:
            print("division by 0")
            _divis_ = 0
        except IndexError:
            print("out of range")
            _divis_ = 0
        finally:
            _newList_.append(_divis_)
    return (_newList_)
