#!/usr/bin/python3
# 12-pascal_triangle.py
"""A python script that
doe the pascal triangle
"""


def pascal_triangle(n):
    """The function doing
    pascal triangle it was beautiful
    and technical to write
    """
    list_of_list = []
    if n <= 0:
        return list_of_list
    else:
        if n == 1:
            list1 = [1]
            list_of_list.append(list1)
            return list_of_list
        else:
            for i in range(n):
                if i == 0:
                    list2 = [1]
                    list_of_list.append(list2)
                else:
                    list3 = list_of_list[i - 1]
                    list4 = []
                    for j in range(i + 1):
                        if j == 0:
                            list4.append(list3[j] + 0)
                        elif j > 0 and len(list3) != j:
                            list4.append(list3[j - 1] + list3[j])
                        else:
                            list4.append(list3[j - 1] + 0)
                    list_of_list.append(list4)
    return list_of_list
