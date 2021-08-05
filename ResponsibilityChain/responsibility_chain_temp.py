from abc import ABCMeta, abstractmethod

class Request(object):
    """请求(内容)"""

    def __init__(self, name, dayoff, reason):
        self.__name = name
        self.__dayoff = dayoff
        self.__reason = reason
        self.__leader = None

    def get_name(self):
        return self.__name

    def get_dayoff(self):
        return self.__dayoff

    def get_reason(self):
        return self.__reason


class Responsible(metaclass=ABCMeta):
    """责任人抽象类"""
    def __init__(self, name, title):
        self.__name = name
        self.__title = title
        self.__next_hander = None
    
    def get_name(self):
        return self.__name

    def get_title(self):
        return self.__title

    def set_next_handler(self, next_handler):
        self.__next_hander = next_handler

    def get_next_handler(self):
        return self.__next_hander

    @abstractmethod
    def _handle_request_impl(self, request):
        pass

    def handle_request(self, request):
        """请求处理"""
        # 当前责任人处理请求
        self._handle_request_impl(request)
        # 如果存在下一个责任人，则将请求传递到下一个责任人
        if self.__next_hander is not None:
            self.__next_hander.handle_request(request)
