#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from py_cn_phone_area_code.skeleton import fib

__author__ = "ZhiFeng Hu"
__copyright__ = "ZhiFeng Hu"
__license__ = "none"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
