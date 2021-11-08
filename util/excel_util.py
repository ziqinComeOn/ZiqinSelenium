#coding =utf-8
import xlrd
from xlutils.copy import copy
import time

class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = "/Users/simufengyun/Desktop/selenium_project/ziqin_selenium/config/casedata.xls"
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)
        self.table = self.data.sheets()[index]    
        #行数
        self.rows = self.table.nrows

    #获取excel数据，按照每行一个list，添加到一个大的list里面
    def get_data(self):
        result = []
        #获取行数
        rows = self.get_lines()
        #只有函数部位None时 才可以for循环
        if rows !=None:
            for i in range(rows):
                col = self.table.row_values(i)
                result.append(col)
            return result   
        return None

    #获取excel行数
    def get_lines(self):
        #行数
        rows = self.table.nrows
        if rows>=1:
            return rows
        return None    
    
    #获取单元格数据
    def get_col_value(self,row,col):
        #如果总行数大于传入的行数 说明有数据可以取到 否则 取不到数据 就要返回None
        if self.get_lines()>row:
            data = self.table.cell(row,col).value
            return data
        return None    

    #写入数据
    def write_value(self,row,value):
        read_value = xlrd.open_workbook(self.excel_path)
        write_data = copy(read_value)
        write_data.get_sheet(0).write(row,9,value)
        write_data.save(self.excel_path)
        time.sleep(1)

if __name__ == '__main__':
    exce = ExcelUtil('/Users/simufengyun/Desktop/selenium_project/ziqin_selenium/config/keyword.xls')
    print(exce.get_col_value(2,3))         