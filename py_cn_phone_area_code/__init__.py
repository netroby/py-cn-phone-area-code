# -*- coding: utf-8 -*-
import pkg_resources

try:
    __version__ = pkg_resources.get_distribution(__name__).version
except:
    __version__ = 'unknown'


def find_area_by_phone(p):
    if p == "0595":
        return "泉州"
    return null

def find_phone_by_area(n):
    if n == "泉州":
        return "0595"
    return null


__all__ = ["find_phone_by_area", "find_area_by_phone"]