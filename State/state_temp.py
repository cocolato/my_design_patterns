from abc import abstractmethod, ABCMeta

class Context(metaclass=ABCMeta):
    """状态模式的上下文环境类"""

    def __init__(self):
        self.__states = []
        self.__cur_state = None
        # 状态发生变化时依赖的属性，当这一变量由多个变量共同决定时可以将其单独定义成一个类
        self.__state_info = 0

    def add_state(self, state):
        if state not in self.__states:
            self.__states.append(state)
    
    def change_state(self, state):
        if state is None:
            return False
        if self.__cur_state is None:
            print(f"初始化为{self.get_state()}")
        else:
            print(f"由{self.__cur_state.get_name()}变为{state.get_name()}")
        self.__cur_state = state
        self.add_state(state)
        return True
    
    def get_state(self):
        return self.__cur_state

    def _set_state_info(self, state_info):
        self.__state_info = state_info
        for state in self.__states:
            if state.is_match(state_info):
                self.change_state(state)

    def _get_state_info(self):
        return self.__state_info


class State:
    """状态的基类"""

    def __init__(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def is_match(self, state_info):
        "状态的属性state_info是否在当前的状态范围内"
        return False

    @abstractmethod
    def behavior(self, Context):
        pass
