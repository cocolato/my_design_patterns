from abc import ABCMeta, abstractmethod
from observer_temp import Observer, Observable


class WashingMode(Observer):
    """该监听模式用于洗澡"""

    def update(self, water_heater, object=0):
        if isinstance(water_heater, WaterHeater):
            cur_temperature = water_heater.get_temperature()
            if 50 <= cur_temperature <= 78:
                print(f"当前水温：{cur_temperature}℃ 可以洗澡了")
        else:
            print("我不能用来监控温度哦!")


class DrinkingMode(Observer):
    """该监听模式用于饮用"""

    def update(self, water_heater, object=0):
        if isinstance(water_heater, WaterHeater):
            cur_temperature = water_heater.get_temperature()
            if cur_temperature >= 100:
                print(f"当前水温：{cur_temperature}℃ 可以饮用了")
        else:
            print("我不能用来监控温度哦!")


class WaterHeater(Observable):
    """热水器"""

    def __init__(self, temperature: int = 25, observers: list = []):
        self.__observers = observers    # 该热水器的观察者
        self.__temperature = temperature  # 热水器初始化温度
        self.notify_observers(self)

    # 获取当前温度
    def get_temperature(self) -> int:
        return self.__temperature

    # 设置温度
    def set_temperature(self, temperature: int):
        self.__temperature = temperature
        print(f"当前温度是：{self.__temperature}℃")
        self.notify_observers(self)

    # 设置监听器
    def add_observer(self, observer: Observer):
        self.__observers.append(observer)

    # 移除监听器
    def remove_observer(self, observe: Observer):
        self.__observers.remove(observe)

    # 触发监听器报警
    def notify_observers(self, object=0):
        for o in self.__observers:
            o.update(self, object)


if __name__ == "__main__":
    heater = WaterHeater(110, [WashingMode(), DrinkingMode()])
    heater.set_temperature(40)
    heater.set_temperature(60)
    heater.set_temperature(80)
    heater.set_temperature(100)
