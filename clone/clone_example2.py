from clone_example1 import Clone

class AppConfig(Clone):
    """应用程序功能配置"""

    def __init__(self, config_name):
        self.__config_name = config_name
        self.parse_from_file("")


    def parse_from_file(self, file_path):
        """
        从配置文件中解析配置项
        真实项目中通常会将配置保存在配置文件中，保证下次开启时依然能生效
        这里为简单起见，不从文件中读取，以初始化的方式来模拟
        """
        
        self.__font_type = "宋体"
        self.__font_size = 13
        self.__language = "中文"
        self.__log_path = "./logs/appException.log"

    def save_to_file(self, file_path):
        """
        将配置保存到配置文件中
        这里为简单起见，不再实现
        """
        pass

    def copy_config(self, config_name):
        """创建一个配置的副本"""
        config = self.deepcopy()
        config.__config_name = config_name
        return config

    def show_info(self):
        print(f"{self.__config_name} 配置信息:")
        print(f"字体: {self.__font_type}")
        print(f"字号: {self.__font_size}")
        print(f"语言: {self.__language}")
        print(f"日志路径: {self.__log_path}")

    def set_font_type(self, font_type):
        self.__font_type = font_type
    
    def set_font_size(self, font_size):
        self.__font_size = font_size

    def set_language(self, language):
        self.__language = language

    def set_log_path(self, log_path):
        self.__log_path = log_path


if __name__ == "__main__":
    default_config = AppConfig("default")
    default_config.show_info()
    print()

    new_config = default_config.copy_config("my_config")
    new_config.set_font_type("黑体")
    new_config.set_font_size(17)
    new_config.set_language("English")
    new_config.show_info()




        

