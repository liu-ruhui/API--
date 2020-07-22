#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:config_demo.py
# @time:2020/7/22 17:10

import os
import configparser

current_value = os.path.dirname(__file__)
config_path = os.path.join(current_value, '..','conf/config.ini')


cfg = configparser.ConfigParser()
cfg.read(config_path,encoding='utf-8')
print(cfg.get('default','URL'))