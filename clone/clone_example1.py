from copy import deepcopy, copy

class Clone(object):
    """克隆的基类"""

    def clone(self):
        return copy(self)

    def deepcopy(self):
        return deepcopy(self)


class Person(Clone):
    """人"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_myself(self):
        print(f"name: {self.name}, age: {self.age}")

    def coding(self):
        print("coding")
    
    def reading(self):
        print("reading")


if __name__ == "__main__":
    jack = Person(name="jack", age=18)
    jack.show_myself()

    
