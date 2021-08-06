from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
    """主题类"""

    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    @abstractmethod
    def request(self, content=""):
        pass


class RealSubject(Subject):
    """真实主题类"""

    def request(self, content):
        print("RealSubject todo something...")


class ProxySubject(Subject):
    """代理主题类"""

    def __init__(self, name, subject):
        super().__init__(name)
        self._real_subject = subject

    def request(self, content):
        self.pre_request()
        if self._real_subject is not None:
            self._real_subject.request(content)
        self.after_request()

    def pre_request(self):
        print("pre request")
    
    def after_request(self):
        print("after request")
