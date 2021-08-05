from responsibility_chain_temp import Responsible, Request

class Person(object):
    """请假者(请假人)"""

    def __init__(self, name):
        self.__name = name
        self.__leader = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_leader(self, leader):
        self.__leader = leader

    def get_leader(self):
        return self.__leader

    def send_reqeust(self, request: Request):
        print(f"{self.__name} 申请请假{request.get_dayoff()}天，请假原因{request.get_reason()}。")
        if self.__leader is not None:
            self.__leader.handle_request(request)
        

class Supervisor(Responsible):
    """主管"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handle_request_impl(self, request: Request):
        if request.get_dayoff() <= 2:
            print(f"同意{request.get_name()}请假，签字人：{self.get_name()}（{self.get_title()}）")


class DepartmentManager(Responsible):
    """部门总监"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handle_request_impl(self, request: Request):
        if request.get_dayoff() > 2 and request.get_dayoff() <= 5:
            print(f"同意{request.get_name()}请假，签字人：{self.get_name()}（{self.get_title()}）")


class CEO(Responsible):
    """CEO"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handle_request_impl(self, request: Request):
        if request.get_dayoff() > 5 and request.get_dayoff() <= 22:
            print(f"同意{request.get_name()}请假，签字人：{self.get_name()}（{self.get_title()}）")


class Administrator(Responsible):
    """行政人员"""

    def __init__(self, name, title):
        super().__init__(name, title)

    def _handle_request_impl(self, request: Request):
        print(f"{request.get_name()}的请假申请已审核，情况属实！已备案处理，处理人：{self.get_name()}（{self.get_title()}）")


if __name__ == "__main__":
    direct_leader = Supervisor("Eren", "客户端研发部经理")
    department_leader = DepartmentManager("Eric", "技术研发中心总监")
    ceo = CEO("Helen", "创新文化公司CEO")
    administrator = Administrator("Nina", "行政中心总监")
    direct_leader.set_next_handler(department_leader)
    department_leader.set_next_handler(ceo)
    ceo.set_next_handler(administrator)

    sunny = Person("sunny")
    sunny.set_leader(direct_leader)
    sunny.send_reqeust(Request(sunny.get_name(), 21, "出国"))




