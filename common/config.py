#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:config业务实现的地方
# @time:2020/7/22 17:29
import os
from common.config_utils import ConfigUtils

current_value = os.path.dirname(__file__)
config_path = os.path.join(current_value, '..','conf/config.ini')
configutils = ConfigUtils(config_path)
URL = configutils.read_value('default','URL')
CASE_DATA_PATH = configutils.read_value('path','CASE_DATA_PATH')


