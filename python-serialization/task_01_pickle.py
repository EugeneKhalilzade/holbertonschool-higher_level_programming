#!/usr/bin/python3
"""
task_01_pickle.py serialize and deserialize python object
using pickle module
"""
import pickle


class CustomObject:
    """
    custom object ...

    __init__ method

    Args:
        name (str): name of the student
        age: age of the student
        is_student: student or not

    Attributes:
        name (str): name of the student
        age: age of the student
        is_student: student or not
    """

    name = ""
    age = 0
    is_student = False

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        displays the attributes of an instance of this class
        """

        obj_dict = self.__dict__

        for key, value in obj_dict.items():
            print(f"{key}: {value}")

    def serialize(self, filename):
        """
        serializes the current instance of the class and save it
        to provided filename

        Args:
            filename (str): name of the file to save serialized data to

        Returns:
            None
        """

        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        load and return an instance of the
        CustomObject from the provided filename

        Args:
            filename (str): name of the file to load from

        Returns:
            An instance of the CustomObject
        """

        data = ""

        try:
            with open(filename, "rb") as file:
                data = pickle.load(file)
        except:
            return None
        return data
