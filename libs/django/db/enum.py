# coding: utf-8

from enum import Enum, unique
from types import DynamicClassAttribute


def first_value_unique(enumeration):
    """ 装饰器：序列的第一个元素唯一 """
    unique(enumeration)
    number_set = set()
    for elem in enumeration:
        first_value = elem.value[0]
        if first_value in number_set:
            raise ValueError('duplicate first value found in %r' % elem)
        number_set.add(first_value)
    return enumeration


class TypeFieldEnum(Enum):
    """ 类型字段枚举类

    示例:
        @first_value_unique
        class XXXEnum(TypeFieldEnum):

            XXX1 = (1, '展示内容1')
            XXX2 = (2, '展示内容2')
            ...
    """

    @classmethod
    def to_tuple(cls):
        """转为元组"""
        return tuple(item.value for item in cls)

    @DynamicClassAttribute
    def val(self):
        """值"""
        return self.value[0]

    @DynamicClassAttribute
    def desc(self):
        """描述"""
        return self.value[1]
