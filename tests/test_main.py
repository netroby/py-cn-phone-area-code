#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from py_cn_phone_area_code import *

__author__ = "ZhiFeng Hu"
__copyright__ = "ZhiFeng Hu"
__license__ = "none"


def test_main():
    assert find_area_by_phone("0595") == "泉州"
    assert find_phone_by_area("泉州") == "0595"
