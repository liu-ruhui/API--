#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:log_utils.py
# @time:2020/7/25 23:09

import os
import logging
import time
from common.localconfig_utils import local_config

current_path = os.path.dirname(__file__)
log_out_path = os.path.join(current_path,'..',local_config.LOG_PATH)

class LogUtils():
    def __init__(self,log_path=log_out_path):
        self.log_name = os.path.join(log_path,'ApiTest_%s.log'%time.strftime('%Y_%m_%d'))
        self.logger = logging.getLogger("ApiTest_")
        self.logger.setLevel(local_config.LOG_LEVEL)
        #  控制台输出
        console_handler = logging.StreamHandler()  #输出到控制台
        file_hander = logging.FileHandler(self.log_name,'a',encoding='utf-8')  #输出到文件，a为追加
        formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")  #设置格式
        console_handler.setFormatter(formatter)
        file_hander.setFormatter(formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_hander)

        console_handler.close()  #防止打印日志重复
        file_hander.close()  #防止打印日志重复

    def get_logger(self):
        return self.logger

logger = LogUtils().get_logger()  #创建好对象，防止打印日志重复

if __name__ == '__main__':
    logger.info("hi")

