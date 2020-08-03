#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:session_demo.py
# @time:2020/7/29 20:39
import requests
import re
from collections import OrderedDict

#用requests完成论坛的发帖

import requests
hosts = 'http://47.107.178.45'
session = requests.session()  #创建session对象

#1.进入论坛首页
res01 = session.get(url=hosts + '/phpwind/')
body01 = res01.content.decode('utf-8')
csrf_token = re.findall('name="csrf_token" value="(.+?)"',body01)[0];

#2.提交用户名和密码
get_parmas = {
    "m":"u",
    "c":"login",
    "a":"dologin"
}
form_data={
    "username":"liuruhui",
    "password":"123456",
    "csrf_token":csrf_token,
    "csrf_token":csrf_token
}
headers = {
    "Accept":"application/json,text/javascript,*/*;q=0.01",
    "X-Requested-With":"XMLHttpRequest",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Content-Type":"application/x-www-form-urlencoded;charset=UTF-8",
    "Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
}
res02 = session.post(url=hosts+'/phpwind/index.php',
                      params = get_parmas,
                      headers = headers,
                      data= form_data
                     )
body02 = res02.content.decode('utf-8')
# print(body02)
login_id = re.findall('_statu=(.+?)"',body02)[0];
# print(login_id)

#3、登陆后的授权
get_params = {
    "m": "u",
    "c": "login",
    "a": "welcome",
    "_statu":login_id
}

res03 = session.get(url=hosts+'/phpwind/index.php',
                    params=get_params
                    )
# print(res03.content.decode('utf-8'))

#4、发帖
get_parmas = {
    "c":"post",
    "a":"doadd",
    "_json":1,
    "fid":57
}
headers_info = {
    "Accept": "application/json,text/javascript,*/*;q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0",
    # "Content-Type": "multipart/form-data; boundary=---------------------------1451597329299",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2"
}
mul_form_data = OrderedDict(
    [
        ("atc_title",(None,'p1p2liu')),
("atc_content",(None,'pppliu')),
("pid",(None,'')),
("tid",(None,'')),
("special",(None,'default')),
("reply_notice",(None,'1')),
("csrf_token",(None,csrf_token)),

    ]
)

res04 = session.post(url=hosts+'/phpwind/index.php',
                     headers = headers_info,
                     params = get_parmas,
                     files = mul_form_data
                     )
print(res04.content.decode('utf-8'))