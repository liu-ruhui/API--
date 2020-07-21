#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:setdefault用法
# @time:2020/7/18 22:27

a = {'one':1,'two':2,'three':3}
#  设置默认值，该key在dict中不存在，新增键值对
a.setdefault('four',4)
#  设置默认值，该key在dict中存在，不会修改dict内容
a.setdefault('one',3.2)
print(a)


lista = [
{'测试用例编号': 'case01', '测试用例名称': '测试能否正确执行获取access_token接口', '用例执行': '是', '测试用例步骤': 'step_01'},
{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_01'},
{'测试用例编号': 'case02', '测试用例名称': '测试能否正确新增用户标签', '用例执行': '否', '测试用例步骤': 'step_02'},
{'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_01'},
{'测试用例编号': 'case03', '测试用例名称': '测试能否正确删除用户标签', '用例执行': '是', '测试用例步骤': 'step_02'}
]
# set_list = {}
# for i in lista:
#     set_list.setdefault(i['测试用例编号'],[]).append(i)  #核心
#     print(set_list)

#更改为{"case_name":"case01","case_info":""}的形式
case_dict = {}
for i in lista:
    case_dict.setdefault(i['测试用例编号'],[]).append(i)

case_list = []
for k,v in case_dict.items(): #items() 方法把字典中每对 key 和 value 组成一个元组，并把这些元组放在列表中返回。
    case_dict = {}
    case_dict["case_name"] = k
    case_dict["case_info"] = v
    case_list.append(case_dict)

for c in case_list:
    print(c)

