#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:取合并单元格的数据
# @time:2020/7/1 21:26
import os
import xlrd
common_value = os.path.dirname(__file__)
data_value = os.path.join(common_value,'data/test_data.xlsx')
wb = xlrd.open_workbook(data_value)  # 创建工作薄对象
sheet = wb.sheet_by_name('Sheet1')  #创建表格对象
cell_value = sheet.cell_value( 0,0 )
print( cell_value )
cell_value = sheet.cell_value( 1,0 )
print( cell_value )
cell_value = sheet.cell_value( 2,0 )  # 合并单元格只有左上角首个单元格才会返回数据
print( cell_value )

# 处理方式：xlrd
merged = sheet.merged_cells  # 返回一个列表  起始行，结束行，起始列，结束列）
print(merged)
# 逻辑： 凡是在merged_cells属性范围内的单元格 它的值都要等于左上角首个单元格的值
# row_index = 0 ; col_index = 0
#
# for (rlow, rhigh, clow, chigh) in merged:  # 遍历表格中所有合并单元格位置信息
#     if (row_index >= rlow and row_index < rhigh):  # 行坐标判断  1<=3<5
#         if (col_index >= clow and col_index < chigh):  # 列坐标判断 0<=0<1
#             # 如果满足条件，就把合并单元格第一个位置的值赋给其它合并单元格
#             cell_value = sheet.cell_value(rlow,clow)
#     else:
#         cell_value = sheet.cell_value(row_index,col_index)
# print( cell_value )
#
def get_merged_cell_value(row_index,col_index):
    '''既能获取普通单元格数据又能获取合并单元格数据'''
    cell_value = None
    for (rlow, rhigh, clow, chigh) in merged:
        if (row_index >= rlow and row_index < rhigh):
            if (col_index >= clow and col_index < chigh):
                cell_value = sheet.cell_value(rlow, clow)
                break; #防止循环的去进行判断出现覆盖的情况
            else:
                cell_value = sheet.cell_value(row_index, col_index)
        else:
            cell_value = sheet.cell_value(row_index,col_index)
    return cell_value

print( get_merged_cell_value(5,0) )

print('-------------------------------')

# 测试
for i in range(1,9):
    print(get_merged_cell_value(i,0))


