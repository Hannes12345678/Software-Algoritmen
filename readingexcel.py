import pandas as pd
import  openpyxl

#pd.__version__




#pd.read_excel('1test1.xlsx')

#pd.read_excel('1test1.xlsx')#, index_col=0

#print(pd.read_excel('1test1.xlsx'))
"""
wb = openpyxl.load_workbook('1test1.xlsx')
print(type(wb))
sheets = wb.sheetnames
print(sheets)
print(wb.active.title)
sh1 = wb['Tabelle1']
data2=wb['Tabelle1']['A2'].value

print(data2)

#print(type(sh1))
print(sh1)
xd=sh1.cell(2,2).value
print(xd)

"""
"""
wb= openpyxl.load_workbook('1test1.xlsx')
#print(wb.active.title)
sh1 = wb[wb.active.title]
row = sh1.max_row
column = sh1.max_column
#print(row)
#print(column)

for i in range(2,row+1):
    for j in range (1,column +1 ):
        print(sh1.cell(i,j).value)
"""
class readplusexcel():

    #def __init__(self, file):
     #   self.file = file

    def dateiausgabe(file):

        wb = openpyxl.load_workbook(file)
        sh1 = wb[wb.active.title]
        row = sh1.max_row
        column = sh1.max_column
        # print(row)
        # print(column)

        for i in range(2, row + 1):
            for j in range(1, column + 1):
                print(sh1.cell(i, j).value)

readplusexcel.dateiausgabe('1test1.xlsx')