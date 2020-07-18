#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:取合并单元格的数据
# @time:2020/7/1 21:26
import os
import xlrd
from common.excel_utils import ExcelUtils

current_value = os.path.dirname(__file__)
excel_path = os.path.join(current_value,'data/testl_data.xlsx')
excelUtils = ExcelUtils(excel_path,"Sheet1")
# print(excelUtils.get_merged_cell_value(8,0))

#自己
# sheet_list = []
# for row in range(1,excelUtils.get_row_count()):
#     dict = {}
#     for col in range(0,excelUtils.get_col_count()):
#         # value = excelUtils.get_merged_cell_value(row,col)
#         dict[excelUtils.get_merged_cell_value(0,col)] =  excelUtils.get_merged_cell_value(row,col)
#     sheet_list.append(dict)

#老师办法
all_data_list = []
first_row = excelUtils.sheet.row(0)
for row in range(1,excelUtils.get_row_count()):
    row_dict = {}
    for col in range(0,excelUtils.get_col_count()):
        row_dict[first_row[col].value] = excelUtils.get_merged_cell_value(row,col)
    all_data_list.append(row_dict)

print('------------------------------')
for row in all_data_list:
    print(row)
