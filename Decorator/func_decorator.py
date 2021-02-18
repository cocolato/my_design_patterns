import logging
logging.basicConfig(level=logging.INFO)

def logging_decorator(func):
    """记录日志的装饰器"""
    def warpper_logging(*args, **kwargs):
        logging.info(f"开始执行{func.__name__}")
        func(*args, **kwargs)
        logging.info(f"{func.__name__}执行完毕！")
    
    return warpper_logging

@logging_decorator
def show_info(*args, **kwargs):
    print("测试")

if __name__ == "__main__":
    show_info()