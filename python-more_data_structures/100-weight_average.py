#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    weight = 0
    try:
        for i in my_list:
            result += i[0] * i[1]
            weight += i[1]
        result = result / weight
    except ZeroDivisionError:
        return 0.0
    finally:
        return result
