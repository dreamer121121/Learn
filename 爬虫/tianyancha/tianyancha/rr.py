import openpyxl
import xlwt
# f = open('suc.txt', 'r')
# data = f.readlines()
# f.close()
# f = open('new_suc.txt','w')
# last = ''
# for item in data:
#     if item != last:
#         f.write(item)
#         last = item
#     else:
#         pass
wb = xlwt.Workbook()
sh = wb.add_sheet('Changelog')

style = xlwt.XFStyle() # 初始化样式
font = xlwt.Font() # 为样式创建字体
font.name = 'Times New Roman'
font.bold = True # 黑体
font.underline = False # 下划线
font.italic = False # 斜体字
style.font = font # 设定样式

f = open('suc.txt', 'r')
data = f.readlines()
index = 1
for item in data:
    item = item.replace("\n", "")
    conetent_list = item.split(',')
    print(conetent_list)
    for i in range(4):
        sh.write(index, i, conetent_list[i], style)
    index += 1

wb.save('changelog.xlsx')