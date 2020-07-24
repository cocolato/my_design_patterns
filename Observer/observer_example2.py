import time
from observer_temp import Observer, Observable

class Account(Observable):
    """用户账户"""
    
    def __init__(self):
        super().__init__()
        self.__latest_ip = dict()
        self.__latest_region = dict()

    def __get_region(self, ip):
        # 通过ip地址获取地区信息
        ipRegion = {
            "101.47.18.9": "浙江省杭州市",
            "67.218.147.69": "美国洛杉矶",
        }
        region = ipRegion.get(ip)
        return "Bad ip address!" if region is None else region

    def __is_long_distance(self, name, region):
        # 计算本次登录与最近几次登录的地区差异
        latest_region = self.__latest_region.get(name)
        return latest_region is not None and latest_region != region

    def login(self, name, ip, time):
        region = self.__get_region(ip)
        if self.__is_long_distance(name, region):
            self.notify_observers({
                "name":   name,
                "ip":     ip,
                "region": region,
                "time":   time,
            })
        self.__latest_region[name] = region
        self.__latest_ip[name] = ip


class SmsSender(Observer):
    """短信发送器"""

    def update(self, observable, object: dict):
        print(f'[短信发送] {object["name"]} 您好！检测到您的账户可能登陆异常。最近一次登录信息: ')
        print(f'登陆地区：{object["region"]}\n登录ip：{object["ip"]}\n登陆时间：{object["time"]}')


class EmailSender(Observer):
    """邮件发送器"""

    def update(self, observable, object: dict):
        print(f'[邮件发送] {object["name"]} 您好！检测到您的账户可能登陆异常。最近一次登录信息: ')
        print(f'登陆地区：{object["region"]}\n登录ip：{object["ip"]}\n登陆时间：{object["time"]}')    


if __name__ == "__main__":
    account = Account()
    account.add_observer(SmsSender())
    account.add_observer(EmailSender())
    account.login("Sam", "101.47.18.9", time.time())
    account.login("Sam", "67.218.147.69", time.time())