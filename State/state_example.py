from state_temp import Context, State


class Water(Context):
    """水(H2O)"""

    def __init__(self):
        super().__init__()
        self.add_state(SolidState("固态"))
        self.add_state(LiquidState("液态"))
        self.add_state(GaseousState("气态"))
        self.set_temperature(25)

    def get_temperature(self):
        return self._get_state_info()

    def set_temperature(self, temperature):
        self._set_state_info(temperature)

    def rise_temperature(self, step):
        self.set_temperature(self.get_temperature()+step)

    def reduce_temperature(self, step):
        self.set_temperature(self.get_temperature()-step)

    def behavior(self):
        state = self.get_state()
        if isinstance(state, State):
            state.behavior(self)


def singleton(cls, *args, **kwargs):
    "单例装饰器"
    instance = {}

    def __singleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]
    return __singleton


@singleton
class SolidState(State):
    """固态"""

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info: int):
        return state_info < 0

    def behavior(self, context: Context):
        print(f"当前状态为固态， 温度：{context._get_state_info()}")


@singleton
class LiquidState(State):
    """液态"""

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info: int):
        return state_info >= 0 and state_info < 100

    def behavior(self, context: Context):
        print(f"当前状态为液态， 温度：{context._get_state_info()}")


@singleton
class GaseousState(State):
    """气态"""

    def __init__(self, name):
        super().__init__(name)

    def is_match(self, state_info: int):
        return 100 <= state_info

    def behavior(self, context: Context):
        print(f"当前状态为气态， 温度：{context._get_state_info()}")


if __name__ == "__main__":
    water = Water()
    water.behavior()
    water.set_temperature(-4)
    water.behavior()
    water.rise_temperature(18)
    water.behavior()
    water.rise_temperature(100)
    water.behavior()
