from proxy_temp import RealSubject, ProxySubject

class TonyReception(RealSubject):
    def __init__(self, name, phone_num):
        super().__init__(name)
        self.__phone_num = phone_num

    def get_phone_num(self):
        return self.__phone_num

    def request(self, content):
        print(f"货物主人:{self.get_name()},手机号:{self.get_phone_num()}")
        print(f"接收到一个包裹,包裹内容:{str(content)}.")


class WendyReception(ProxySubject):
    def __init__(self, name, reciver):
        super().__init__(name, reciver)

    def pre_request(self):
        print(f"代{self._real_subject.get_name()}收包裹")

    def after_request(self):
        print(f"代收人:{self.get_name()}")


if __name__ == "__main__":
    tony = TonyReception("tony", 123456)
    tony.request("SONY PS5")

    wendy = WendyReception("wendy", tony)
    wendy.request("SONY PS5")

    