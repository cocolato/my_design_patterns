from abc import ABCMeta, abstractmethod
from enum import Enum

class DeviceType(Enum):
    """设备类型"""

    TypeSpeaker = 1
    TypeMicroPhone = 2
    TypeCamera = 3

class DeviceItem:
    """设备项"""

    def __init__(self, id, name, type, is_defalut=False):
        self.__id = id
        self.__name = name
        self.__type = type
        self.__is_default = is_defalut

    def __str__(self):
        return f"type:{self.__type}\nid:{self.__id}\nname:{self.__name}\nis_default:{self.__is_default}"
    
    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__type
    
    def is_defalut(self):
        return self.__is_default


class DeviceList:
    """设备列表"""

    def __init__(self):
        self.__devices = []

    def add(self, device_item):
        self.__devices.append(device_item)

    def get_count(self):
        return len(self.__devices)
    
    def get_by_idx(self, idx):
        try:
            return self.__devices[idx]
        except Exception as e:
            return None
    
    def get_by_id(self, id):
        for item in self.__devices:
            if item.get_id() == id:
                return item
        return None

    
class DeviceMgr(metaclass=ABCMeta):
    @abstractmethod
    def enumerate(self):
        """枚举设备列表"""
        pass

    @abstractmethod
    def active(self, device_id):
        """选择需要使用的设备id"""
        pass

    @abstractmethod
    def get_cur_device_id(self):
        """获取当前使用的设备id"""
        pass

class SpeakerMgr(DeviceMgr):
    """扬声器设备管理类"""

    def __init__(self):
        self.__cur_device_id = None
    
    def enumerate(self):
        devices= DeviceList()
        devices.add(DeviceItem("369dd760", "Realtek High Definition Audio", DeviceType.TypeSpeaker))
        devices.add(DeviceItem("59357638", "NVDIA High Definition Audio", DeviceType.TypeSpeaker, True))
        return devices
    
    def active(self, device_id):
        self.__cur_device_id = device_id
    
    def get_cur_device_id(self):
        return self.__cur_device_id


class DeviceUtil:
    """设备工具类"""

    def __init__(self):
        self.__mgrs = {
            DeviceType.TypeSpeaker: SpeakerMgr()
        }

    def __get_device_mgr(self, type):
        return self.__mgrs[type]
    
    def get_device_list(self, type):
        return self.__get_device_mgr(type).enumerate()
    
    def active(self, type, device_id):
        self.__get_device_mgr(type).active(device_id)
    
    def get_cur_device_id(self, type):
        return self.__get_device_mgr(type).get_cur_device_id()

if __name__ == "__main__":
    device_util = DeviceUtil()
    device_list = device_util.get_device_list(DeviceType.TypeSpeaker)
    print("麦克风设备列表：")
    if device_list.get_count() > 0:
        device_util.active(DeviceType.TypeSpeaker, device_list.get_by_idx(0).get_id())
    for idx in range(0, device_list.get_count()):
        device = device_list.get_by_idx(idx)
        print(device)
    print(f"当前使用的设备:{device_list.get_by_id(device_util.get_cur_device_id(DeviceType.TypeSpeaker)).get_name()}")
