def singleton_decorator(cls, *args, **kwargs):
    """定义单例装饰器"""
    instance = {}

    def wrapper_singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return wrapper_singleton


@singleton_decorator
class Singleton:

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name


if __name__ == "__main__":
    tony = Singleton("Tony")
    karry = Singleton("Karry")
    print(id(tony), id(karry))
