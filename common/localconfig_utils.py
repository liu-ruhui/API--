#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:配置文件的方式二
# @time:2020/7/22 21:47
import os
import configparser
current_value = os.path.dirname(__file__)
config_path = os.path.join(current_value, '..','conf/config.ini')

class LocalconfigUtils():
    def __init__(self,config_path =config_path ):
        self.cfg = configparser.ConfigParser()
        self.cfg.read(config_path,encoding='UTF-8')

    @property  #把方法变成属性方法
    def URL(self):
        url_value = self.cfg.get('default','URL')
        return url_value

    @property
    def CASE_DATA_PATH(self):
        case_data_path_value = self.cfg.get('path','CASE_DATA_PATH')
        return case_data_path_value

local_config = LocalconfigUtils()
if __name__ =="__main__":
    config = LocalconfigUtils()
    print(config.URL)  #config.URL()