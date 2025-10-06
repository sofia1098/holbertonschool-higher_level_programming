#!/usr/bin/python3
""""pickle """


import pickle


class CustomObject:
    """ clase """
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception as err:
            print(f"Serialization failed: {err}")

    @classmethod
    def deserialize(cls, filename: str):
        try:
            with open(filename, "rb") as f:
                objeto = pickle.load(f)
                if isinstance(objeto, cls):
                    return objeto
                else:
                    print("Error: The deserialized object is not a CustomObject.")
                    return None
        except Exception as err:
            print(f"Deserialization failed: {err}")
            return None
