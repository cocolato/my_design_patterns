from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    """观察者的基类"""

    # 待实现的通知方法
    @abstractmethod
    def update(self, observable, object):
        pass


class Observable:
    """被观察者的基类"""

    def __init__(self):
        self.__observers = []

    # 设置监听者
    def add_observer(self, observer):
        self.__observers.append(observer)

    # 移除监听者
    def remove_observer(self, observer):
        self.__observers.remove(observer)
    
    # 触发监听者的通知方法
    def notify_observers(self, object=0):
        for observer in self.__observers:
            observer.update(self, object)
