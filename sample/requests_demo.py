#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:requests_demo.py
# @time:2020/7/27 16:24

import requests

hosts = 'https://api.weixin.qq.com'
#  获取token
params = {
    'grant_type':'client_credential',
    'appid':'wx8d284df159a5ab45',
    'secret':'36291ac0b1dac204d5a1928252781ea3'
}
rest01 = requests.get(url=hosts+'/cgi-bin/token',
                      params=params
                      )
token_id = rest01.json()['access_token']
print(rest01.json())

#  创建一个标签
get_params = {
    'access_token':token_id
}
post_params = '{   "tag" : {    "name" : "newdream112"  } }'
headers = {
    'content_type':'application/json'
}
rest02 = requests.post(url = hosts+'/cgi-bin/tags/create',
                       params = get_params,
                       data = post_params,
                       headers = headers
                       )
print(rest02.json())