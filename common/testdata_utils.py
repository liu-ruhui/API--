#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:testdata_utils.py
# @time:2020/7/18 23:51

import os
from common.excel_utils import ExcelUtils
current_path = os.path.dirname(__file__)
test_data_file = os.path.join(current_path,'..','test_data/test_case.xlsx')

class TestdataUtils():
    def __init__(self,test_data_path = test_data_file):
        self.test_data_path = test_data_path
        self.test_data = ExcelUtils(test_data_path,"Sheet1").get_sheet_data_by_dict() #获取sheet1的所有数据

    def __get_testcase_data_dict(self):
        testcase_dict = {}
        for row_data in self.test_data:
            testcase_dict.setdefault(row_data['测试用例编号'],[]).append(row_data)
        return testcase_dict

    def get_testcase_data_list(self):
        testcase_list = []
        for key,value in self.__get_testcase_data_dict().items():
            one_case_dict={}
            one_case_dict["case_name"]=key
            one_case_dict["case_info"]=value
            testcase_list.append(one_case_dict)
        return testcase_list


if __name__ == "__main__":
    testdataUtils = TestdataUtils()
    # print(testdataUtils.get_testcase_data())
    for i in testdataUtils.get_testcase_data_list():
        print(i)

