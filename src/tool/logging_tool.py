# -*- coding: utf-8 -*-
# @author: caoyang
# @email: caoyang@163.sufe.edu.cn
import logging


# 初始化日志配置
def initialize_logger(filename, mode='w'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s | %(filename)s | %(levelname)s | %(message)s')
    file_handler = logging.FileHandler(filename, mode=mode, encoding='utf8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)
    logger.addHandler(console)
    return logger


# 终止日志句柄
def terminate_logger(logger):
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
