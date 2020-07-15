from abc import ABCMeta, abstractmethod


class Observer(metaclass=ABCMeta):
    """监听器的父类"""

    # 待实现的通知方法
    @abstractmethod
    def update(self, waterHeater):
        pass


class WashingMode(Observer):
    """该监听模式用于洗澡"""

    def update(self, waterHeater):
        cur_temperature = waterHeater.get_temperature()
        if 50 <= cur_temperature <= 78:
            print(f"当前水温：{cur_temperature}℃ 可以洗澡了")


class DrinkingMode(Observer):
    """该监听模式用于饮用"""

    def update(self, waterHeater):
        cur_temperature = waterHeater.get_temperature()
        if 100 <= cur_temperature:
            print(f"当前水温：{cur_temperature}℃ 可以饮用了")


class WaterHeater:
    """热水器"""
    
    def __init__(self, temperature: int=25, observers: list=[]):
        self.__observers = observers    # 该热水器的观察者
        self.__temperature = temperature  # 热水器初始化温度
        self.notifies()

    # 获取当前温度
    def get_temperature(self)-> int:
        return self.__temperature
    
    # 设置温度
    def set_temperature(self, temperature: int):
        self.__temperature = temperature
        print(f"当前温度是：{self.__temperature}℃")
        self.notifies()
    
    # 设置监听器
    def add_observer(self, observer: Observer):
        self.__observers.append(observer)
    
    # 触发监听器报警
    def notifies(self):
        for o in self.__observers:
            o.update(self)
    

if __name__ == "__main__":
    heater = WaterHeater(110, [WashingMode(), DrinkingMode()])
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(80)
    heater.set_temperature(100)
