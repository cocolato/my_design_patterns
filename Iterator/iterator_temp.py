class BaseIterator(object):
    """迭代器"""

    def __init__(self, data):
        self.__data = data
        self.__cur_idx = 0

    def to_begin(self):
        self.__cur_idx = 0

    def to_end(self):
        self.__cur_idx = -1

    def next(self):
        if self.__cur_idx >= 0 and self.__cur_idx < len(self.__data) - 1:
            self.__cur_idx += 1
            return True
        return False

    def previous(self):
        if self.__cur_idx > 0 and self.__cur_idx < len(self.__data):
            self.__cur_idx -= 1
            return True
        return False

    def current(self):
        return self.__data[self.__cur_idx] if self.__cur_idx >= 0 and self.__cur_idx < len(self.__ldata) else None