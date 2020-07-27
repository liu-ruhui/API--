#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:log_demo.py
# @time:2020/7/25 21:28

import logging

logger = logging.getLogger("logger")

hander1 = logging.StreamHandler()
logger.setLevel(10)  #notset(0)  debug(10)  info(20)  warning(30)  error(40)  critical(50
formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
hander1.setFormatter(formatter)
logger.addHandler(hander1)

hander2 = logging.FileHandler('./test.log','a',encoding='utf-8')  #a表示追加
hander2.setLevel(10) #设置为局部 或logging.DEBUG
hander2.setFormatter(formatter)
logger.addHandler(hander2)

logger.info("hello")