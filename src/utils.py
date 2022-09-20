# -*- coding: utf-8 -*-
# @author : caoyang
# @email: caoyang@163.sufe.edu.cn
# 其他工具函数

import time
from functools import wraps


# 程序计时的装饰器
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        function_return = func(*args, **kwargs)
        end_time = time.time()
        print('Function `{}` runtime is {} seconds.'.format(function.__name__, end_time - start_time))
        return function_return
    return wrapper
