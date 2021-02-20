class Singleton(object):
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            Singleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            Singleton.__isFirstInit = True

    def getName(self):
        return self.__name

if __name__ == "__main__":
    tony = Singleton("Tony")
    karry = Singleton("Karry")
    print(id(tony), id(karry))
