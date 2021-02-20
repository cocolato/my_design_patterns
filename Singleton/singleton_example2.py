class Singleton(type):

    def __init__(cls, what, bases=None, dict=None):
        super().__init__(what, bases, dict)
        cls._instance = None
    
    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class CustomClass(metaclass=Singleton):
    def __init__(self, name):
       pass

if __name__ == "__main__":
    tony = CustomClass("Tony")
    karry = CustomClass("Karry")
    print(id(tony), id(karry))